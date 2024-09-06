
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # count unique characters in all strings
    char_counts = {}
    for word in words:
        for c in word:
            if c not in char_counts:
                char_counts[c] = 1
            else:
                char_counts[c] += 1
    max_char = max(char_counts, key=char_counts.get)

    # check if there are multiple strings with max number of unique characters
    if max_char > 1:
        # sort words by their frequency of each character
        word_frequencies = {}
        for word in words:
            word_chars = [c for c in word if c in char_counts]
            word_frequencies[word] = char_counts[word_chars[0]]
        sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

        return sorted_words[0][0]
    else:
        return max_char
