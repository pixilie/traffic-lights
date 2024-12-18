{
  inputs = { nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.11"; };

  outputs = { self, nixpkgs }:
    let
      inherit (nixpkgs.lib) genAttrs;

      forAllSystems =
        genAttrs [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" ];
      forAllPkgs = function: forAllSystems (system: function pkgs.${system});

      pkgs = forAllSystems (system:
        (import nixpkgs {
          inherit system;
          overlays = [ ];
        }));
    in {
      formatter = forAllPkgs (pkgs: pkgs.nixpkgs-fmt);

      devShells = forAllPkgs (pkgs:
        with pkgs.lib;
        let
          python-env = (pkgs.python312.withPackages
            (ps: with ps; [ ipython python-lsp-server ]));
        in {
          default = pkgs.mkShell rec {
            nativeBuildInputs = with pkgs; [
              python-env
              ruff
              ruff-lsp
              python312Packages.jedi
            ];
            buildInputs = with pkgs; [
              python312Packages.pygame
              python312Packages.tkinter
            ];

            LD_LIBRARY_PATH = makeLibraryPath buildInputs;
          };
        });
    };
}

