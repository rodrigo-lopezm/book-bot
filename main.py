from stats import *
import sys


def get_book_text(relpath : str) -> str:
    with open(relpath, "r") as f:
        file_contents = f.read()
        return file_contents

def print_report(relpath : str, wordcount : int, sortedwlist : list[tuple[str,int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relpath}...")
    print("------------ Word count -----------")
    print(f"Found {wordcount} total words")
    print("------------ Character count -----------")
    for char in sortedwlist:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
def main():
    if len(sys.argv) >= 2:
        RelativePath = sys.argv[1]
        BookExtract = get_book_text(RelativePath)
        WordCount = countwords(BookExtract)
        SortedList = chars_dict_to_sorted_list(convtodict(BookExtract))
        print_report(RelativePath, WordCount, SortedList)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
