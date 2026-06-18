import sys
from pathlib import Path
from bs4 import BeautifulSoup


def format_html_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(text, "html.parser")
    formatted = soup.prettify(formatter="html")
    path.write_text(formatted, encoding="utf-8")


def main() -> int:
    # If no arguments provided, format all .html files in the current directory.
    args = sys.argv[1:]
    if not args:
        cwd = Path('.').resolve()
        args = [str(p) for p in cwd.glob('*.html')]
        if not args:
            print("No .html files found in the current directory.")
            return 1

    for arg in args:
        path = Path(arg)
        if not path.exists():
            print(f"File not found: {path}")
            continue
        print(f"Formatting {path}")
        format_html_file(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
