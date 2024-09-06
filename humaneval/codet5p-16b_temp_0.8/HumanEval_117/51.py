
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

    vowels = set('aeiou')
    result = []
    for i in range(len(s)):
        if s[i] not in vowels:
            if i + 1 == len(s):
                result.append(s[i : i + n])
            else:
                result.append(s[i : i + n])
                for j in range(i + 1, len(s)):
                    if s[j] not in vowels:
                        if j + 1 == len(s):
                            result.append(s[i : j + n])
                        else:
                            result.append(s[i : j + n])
                            for k in range(j + 1, len(s)):
                                if s[k] not in vowels:
                                    if k + 1 == len(s):
                                        result.append(s[i : k + n])
                                    else:
                                        result.append(s[i : k + n])
                                        for l in range(k + 1, len(s)):
                                            if s[l] not in vowels
