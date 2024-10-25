word_count = 0
char_count = {}
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(file_content)

    words = file_content.split()
    word_count = len(words)
    print(f"{word_count} words found in the document")

    lowered_file = file_content.lower()
    for char in lowered_file:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    print(char_count)


main()
