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
    "cheyinchu": "def",  # Function definition
    "pampu": "input",  # User input
    "lekka": "len",  # Length of list
    "modhati": "and",  # Logical AND
    "ledu": "or",  # Logical OR
    "kaadu": "not",  # Logical NOT
    "file_thervu": "open",  # File Handling - Open File
    "file_chaduvu": "read",  # File Handling - Read File
    "file_rayu": "write",  # File Handling - Write File
    "file_muyu": "close",  # File Handling - Close File
    "prayathninchu": "try",  # Exception Handling - Try
    "minyaimpu": "except",  # Exception Handling - Except
    "vargam":"class"# opp-class defination
    "vastuvu":"self"#opp-object defination
    "listu"="list" #list
    "nighantuvu": "dict"  # Dictionaries
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
        print("పొరపాటు జరిగింది:", e)  # Error message in Telugu

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("వినియోగం: python telugulang.py <filename.tl>")
    else:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            code = file.read()
            run_telugulang(code)
