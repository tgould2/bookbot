def get_num_words(text):
    """Count the number of words in the text."""
    words = text.split()
    return len(words)


def get_book_text(path):
    """Read the book content from a file."""
    with open(path) as f:
        return f.read()


def get_chars_dict(text):
    """Count the occurrences of each character in the text, case insensitive."""
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    # Get the character counts as a dictionary
    char_counts = get_chars_dict(text)

    # Convert dictionary to a list of tuples (character, count)
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the sorted character counts
    for char, count in sorted_chars:
        print(f"{char}: {count}")


# Run the main function
main()
