
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

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    consonants = set()
    words = list()
    
    if n == 0:
        return list()
    
    if len(s) == 0:
        return list()
    
    if n > len(s):
        return list()
    
    s = s.lower()
    
    for i in range(len(s)):
        if s[i] not in vowels:
            consonants.add(s[i])
    
    for i in range(len(s)):
        if len(consonants) == n:
            words.append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in consonants:
                    words.append(s[j])
                else:
                    break
            break
    
    return words












































    
    
    
    
    
    
