
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
    # User code goes here
    def is_consonant(char):
        return char in 'bcdfghjklmnpqrstvwxyz'

    def is_vowel(char):
        return char in 'aeiou'

    if n == 0 or n == -1 or n > len(s):
        return []
    
    result = []
    for i in range(len(s)):
        if i == 0:
            if is_consonant(s[0]):
                result.append(s[0])
                continue
        if i > 0:
            if is_consonant(s[i]) and not is_vowel(s[i-1]):
                result.append(s[i])
            elif is_consonant(s[i]) and is_vowel(s[i-1]):
                result.append(s[i])
    
    return result
