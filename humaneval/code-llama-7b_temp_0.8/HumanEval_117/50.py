
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
    #my code
    def check_consonant(char):
        if char not in 'aeiou':
            return True
    s = s.split()
    result = []
    for i in range(len(s)):
        if len([check_consonant(char) for char in s[i]]) == n:
            result.append(s[i])
    return result


    #leetcode
    def check_consonant(char):
        if char not in 'aeiou':
            return True

    s = s.split()
    res = []
    for word in s:
        if len([check_consonant(char) for char in word]) == n:
            res.append(word)
    return res

    #s = s.split()
    #return [s[i] for i in range(len(s)) if len([c for c in s[i] if c not in 'aeiou']) == n]
    #return [s[i] for i in range(len(s)) if len([c for c in s[i] if c not in 'aeiou']) == n]
















    #best way
    def check_consonant(char):
        if char not in 'aeiou':
            return True

    s = s.split()
    res = []
    for word in s:
        if len([check_consonant(char) for char in word]) == n:
            res.append(word)
    return res


    #best way
    def check_consonant(char):
        if char not in 'aeiou':
            return True
    s = s.split()
    res = []
    for word in s:
        if len([check_consonant(char) for char in word]) == n:
            res.append(word)
    return res





















































