
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    def count_unique_characters(word):
        unique_characters = set()

        for character in word:
            if character in unique_characters:
                continue

            unique_characters.add(character)

        return len(unique_characters)

    max_length = max(count_unique_characters(word) for word in words)
    max_length_words = [word for word in words if count_unique_characters(word) == max_length]

    if not max_length_words:
        return ""

    return sorted(max_length_words)[0]
