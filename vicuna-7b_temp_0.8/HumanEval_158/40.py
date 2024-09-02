
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    def count_chars(word):
        count = 0
        for char in word:
            if char in "aeiouAEIOU":
                count += 1
            elif char in "bcdfghjkmnpqrstvwXYZ":
                count += 2
            else:
                count += 1
        return count

    def count_words_chars(word):
        count = 0
        for char in word:
            if char in "aeiouAEIOU":
                count += 1
            elif char in "bcdfghjkmnpqrstvwXYZ":
                count += 2
            else:
                count += 1
        return count

    def sort_word(word):
        word = word.lower()
        return "".join([word[i:i+1] for i in range(0, len(word), 1)])

    max_word = []
    max_chars = []

    for word in words:
        word = word.lower()
        unique_chars = set(count_chars(word))
        unique_words = set(count_words_chars(word))

        if len(unique_chars) == 1:
            max_chars.append(max_chars[0])
            max_chars.append(unique_chars.pop())
            if len(unique_words) == 1:
                max_word.append(max_chars)
                max_chars = []
                max_word.append(word)
            else:
                max_word.append(word)
        elif len(unique_words) == 1:
            max_chars.append(max_chars[0])
            max_chars.append(unique_words.pop())
            max_word.append(word)
        else:
            max_chars.append(max_chars[0])
            max_chars.append(unique_words.pop())
            max_chars.append(unique_chars.pop())
            max_word.append(word)

    if len(max_chars) == 
