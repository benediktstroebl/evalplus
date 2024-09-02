
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
    words = [s[i:i+1] for i in range(len(s)-1)]
    n_consonants = [c for c in s if c.isalpha() and (ord(c) >= ord('b') and ord(c) <= ord('p'))]
    result = []
    for i in range(len(words)-1):
        if len(n_consonants) == 1 and n_consonants[0] in words[i:i+1]:
            result.append(words[i])
        elif len(n_consonants) == 2 and n_consonants[0] in words[i:i+1] and n_consonants[1] in words[i:i+1]:
            result.append(words[i])
        elif len(n_consonants) == 3 and n_consonants[0] in words[i:i+1] and n_consonants[1] in words[i:i+1] and n_consonants[2] in words[i:i+1]:
            result.append(words[i])
        elif len(n_consonants) == 4 and n_consonants[0] in words[i:i+1] and n_consonants[1] in words[i:i+1] and n_consonants[2] in words[i:i+1] and n_consonants[3] in words[i:i+1]:
            result.append(words[i])
    return result
