def find_max(words):
    # Initialize the list of unique characters and the word with the most unique characters
    unique_chars = []
    max_word = ""

    # Add all the words and characters to the list of unique characters
    for word in words:
        for char in word:
            unique_chars.append(char)

    # Find the maximum word with the most unique characters
    word = "".join()
    for char in unique_chars:
        if char > " ":
            word += char
    return word