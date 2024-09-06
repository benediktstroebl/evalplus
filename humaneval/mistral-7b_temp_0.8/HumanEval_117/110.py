
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
    # if len(s) == 0:
    #     return []
    # else:
    #     words = []
    #     for i in range(len(s)):
    #         if s[i].isalpha() and s[i] != ' ':
    #             word = ''
    #             while s[i].isalpha():
    #                 word += s[i]
    #                 i += 1
    #             words.append(word)
    #             if len(words[-1]) == n:
    #                 return words
    # return words

    word = ''
    words = []
    for i in range(len(s)):
        if s[i].isalpha() and s[i] != ' ':
            word = ''
            while s[i].isalpha():
                word += s[i]
                i += 1
            words.append(word)
    count = 0
    for i in range(len(words)):
        if len(words[i]) == n:
            count += 1
    if count != 
