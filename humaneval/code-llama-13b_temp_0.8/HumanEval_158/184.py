
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    # ...

    # to compare the list (lexicographical order) and return the first one
    # that meets the maximum unique characters criteria

    # check the length of each string and check if is bigger than the first
    # string in the list

    max_word = words[0]
    count = 0
    for word in words:
        if len(word) > len(max_word):
            max_word = word
        count += 1
        # check for maximum unique characters
        if len(max_word) != len(set(max_word)):
            max_word = words[count]
            # check for lexicographical order
            while len(max_word) == len(set(max_word)) and max_word != words[-1]:
                if max_word > words[count + 1]:
                    max_word = words[count + 1]
                    count += 1
                elif max_word < words[count + 1]:
                    break
            break
    return max_word

