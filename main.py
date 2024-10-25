word_count = 0
char_count = {}
book_path = "books/frankenstein.txt"
def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
       

    words = file_content.split()
    word_count = len(words)
    print(f"The book report of {book_path}")
    print(f"{word_count} words found in the document")

    lowered_file = file_content.lower()
    for char in lowered_file:
        if char.isalpha():
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char] = 1
    
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_chars:
        print(f"The {char} character was found {count} times")       

main()
