
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """

    def get_words_list(s, n):
        result = []
        i = 0
        while i < len(s):
            word = ""
            while s[i] != " " and i < len(s):
                word += s[i]
                i += 1
            if len(word) == n:
                result.append(word)
            i += 1
        return result

    def get_word_without_vowels(word):
        result = ""
        for char in word:
            if char not in "aeiouAEIOU":
                result += char
        return result

    result = []
    words = get_words_list(s, n)
    for word in words:
        if get_word_without_vowels(word) == word:
            result.append(word)
    return result

