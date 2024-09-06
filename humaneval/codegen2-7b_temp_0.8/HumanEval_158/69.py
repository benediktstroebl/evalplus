
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    dict_chars = {x:0 for x in words}
    for word in words:
        for char in word:
            dict_chars[char]+=1
    max_word = ""
    max_num = 0
    for word, num in dict_chars.items():
        if num > max_num:
            max_word = word
            max_num = num
    return max_word
