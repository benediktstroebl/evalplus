def select_words(s, n):
    '''
    Given a string s and a natural number n, return a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    '''
    # empty case
    if not s:
        return []
    # dictionary to count consonants
    d = {}
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    words = []
    
    # iterate over spaces to get words
    for i in range(len(s)):
        if s[i] == ' ':
            word = s[0:i]
            if len(word) == 0:
                continue
            # count consonants
            c = 0
            for letter in word:
                if letter in consonants:
                    c += 1
            # store word and count
            if c == 0 or (c>0 and c==n):
                words.append(word)
            # reset count
            c = 0
    return words