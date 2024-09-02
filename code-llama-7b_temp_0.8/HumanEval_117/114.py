
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
    words = s.split()
    # # O(n^2) time | O(n) space
    # vowels = "aeiou"
    # res = []
    # for word in words:
    #     count = 0
    #     for letter in word:
    #         if letter not in vowels:
    #             count += 1
    #     if count == n:
    #         res.append(word)
    # return res

    # O(n^2) time | O(n) space
    vowels = "aeiou"
    res = []
    for word in words:
        count = 0
        for letter in word:
            if letter not in vowels:
                count += 1
        if count == n:
            res.append(word)
    return res

    # O(n) time | O(n) space
    vowels = "aeiou"
    res = []
    i = 0
    while i < len(s):
        curr_word_start = i
        while i < len(s) and s[i] not in vowels:
            i += 1
        if i - curr_word_start == n:
            res.append(s[curr_word_start:i])
        while i < len(s) and s[i] in vowels:
            i += 1
    return res
