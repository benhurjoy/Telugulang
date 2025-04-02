import re
import sys

# Telugu Keywords Mapping
keywords = {
    "mudrinchu": "print",
    "okavela": "if",
    "ayithe": "while",
    "thirigistha": "return",
    "apey": "break",
    "kudika": "+",
    "thisivetha": "-",
}

def translate_line(line):
    """Translate Telugu syntax to Python syntax"""
    for telugu, english in keywords.items():
        line = line.replace(telugu, english)
    return line

def run_telugulang(code):
    """Execute TeluguLang code"""
    translated_code = "\n".join([translate_line(line) for line in code.split("\n")])
    try:
        exec(translated_code)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python telugulang.py <filename.tl>")
    else:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            code = file.read()
            run_telugulang(code)
