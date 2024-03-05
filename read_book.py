def count_words(text):
    # Splits the text into words using whitespace as the delimiter
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    letter_counts = {}
    for char in text:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    # Sort by character alphabetically
    letter_count_list = [{"char": char, "count": count} for char, count in letter_counts.items()]
    letter_count_list.sort(key=lambda x: x["char"])  # Sorting alphabetically by character

    return letter_count_list


    # Iterate over each character in the text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts


def main():
    path_to_file = 'books/frankenstein.txt'

    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    letter_count_list = count_letters(file_contents)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")

    for letter in letter_count_list:
        print(f"The '{letter['char']}' character was found {letter['count']} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()
