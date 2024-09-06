
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
    # Save the start and end indices of each consonant
    # in the word.
    consonants = set()
    for i in range(len(s)):
        if s[i] == 'c':
            consonants.add(i)
        elif s[i] == 'C':
            consonants.add(len(s) - i - 1)
        elif s[i] == 's':
            consonants.add(i)
        elif s[i] == 'S':
            consonants.add(len(s) - i - 1)
        elif s[i] == 't':
            consonants.add(i)
        elif s[i] == 'T':
            consonants.add(len(s) - i - 1)
        elif s[i] == 'p':
            consonants.add(i)
        elif s[i] == 'P':
            consonants.add(len(s) - i - 1)
        elif s[i] == 'n':
            consonants.add(i)
        elif s[i] == 'N':
            consonants.add(len(s) - i - 1)
        elif s[i] == 'i':
            consonants.add(i)
        elif s[i] == 'I':
            consonants.add(len(s) - i - 1)
        elif s[i] == 'u':
            consonants.add(i)
        elif s[i] == 'U':
            consonants.add(len(s) - i - 1)
        elif s[i] == 'r':
            consonants.add(i)
        elif s[i] == 'R':
            consonants.add(len(s) - i - 1)
        elif s[i] == 'm':
            consonants.add(i)
        elif s[i] == 'M':
            consonants.add(len(s) - i - 1)
        elif s[i] == 'd':
            consonants.add(i)
       
