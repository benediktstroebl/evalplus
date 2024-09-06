
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # Your code here
    list_of_words_with_unique_chars = []
    for word in words:
        list_of_words_with_unique_chars.append([word, len(set(word))])
    sorted_words = sorted(list_of_words_with_unique_chars, key=lambda x: x[1], reverse=True)
    return sorted_words[0][0]




