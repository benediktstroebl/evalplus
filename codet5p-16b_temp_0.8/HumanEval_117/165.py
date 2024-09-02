
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

    from string import ascii_lowercase, ascii_uppercase

    words = []
    consonants = ""
    for letter in s:
        if letter not in consonants and letter!= " ":
            consonants += letter
    consonants = ascii_lowercase.replace(consonants, "")
    if consonants == "":
        return []
    for i in range(len(s)):
        if len(consonants) == n:
            words.append(s[i:].split()[0])
        if s[i] in consonants and len(consonants) < n:
            s = s[:i] + s[i+1:]
            if len(consonants) == n:
                words.append(s.split()[0])
            else:
                consonants = consonants.replace(s[i], "")
    return words
