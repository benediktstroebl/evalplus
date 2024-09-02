
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
    if len(s) == 0:
        return []
    else:
        n = len(s) - n
        result = []
        for i in range(1, len(s)):
            if s[i] == ' ' and (i != 0 or n % 2 == 0):
                result.append(s[i])
            if (s[i] == ' ' and n % 2 == 0) or (s[i] == 'z' or s[i] == 'Z') or (s[i] == 'x' or s[i] == 'X') or (s[i] == 'c' or s[i] == 'C') or (s[i] == 'g' or s[i] == 'G') or (s[i] == 'q' or s[i] == 'Q') or (s[i] == 'p' or s[i] == 'P') or (s[i] == 'o' or s[i] == 'O'):
                result.append(s[i])
        result.extend(result[:-1])
        return result
        