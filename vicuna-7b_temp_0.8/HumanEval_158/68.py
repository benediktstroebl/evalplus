
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    max_word = ""
    max_chars = {}
    for word in words:
        chrs = [letter.lower() for letter in word]
        chrs_count = sum([1 for char in chrs if char in chrs_count])
        if max_chars[chrs_count] is None:
            max_chars[chrs_count] = len(chrs)
        else:
            max_chars[chrs_count] = max(max_chars[chrs_count], len(chrs))
        if word not in max_word:
            max_word.append(word)
        if max_chars[chrs_count] > max_word_chars[max_word_len]:
            max_word = word
            max_word_len = chrs_count
    return max_word