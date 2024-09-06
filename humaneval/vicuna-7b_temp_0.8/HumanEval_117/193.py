
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
    # check if the input string is empty or not
    if len(s) == 0:
        return []
    # check if the input string is of length 1 or not
    if len(s) == 1:
        return [s]
    # initialize an empty list to store the words
    words = []
    # loop through all characters of the input string
    for i in range(len(s)):
        # check if the current character is a consonant or not
        if s[i] == 'c':
            # check if the previous character is a consonant or not
            if i > 0 and s[i-1] == 'c':
                # check if the word contains exactly n consonants or not
                if (i-2) < len(s) and s[i-2] == 'c':
                    # check if the word contains exactly n-1 consonants or not
                    if (i-3) < len(s) and s[i-3] == 'c':
                        # if word contains exactly n consonants then append it to the list
                        words.append(s[i-2:i+1])
                        # remove the word from the string
                        s = s[:i-2] + s[i+1:]
                        # check if the word is still valid or not
                        if (i+1) < len(s) and s[i] == 'c':
                            # if the word is still valid then append it to the list
                            words.append(s[i:i+2])
                            # remove the word from the string
                            s = s[:i] + s[i+2:]
                            # check if the word is still valid or not
                            if (i+2) < len(s) and s[i+2] == 'c':
                                # if the word is still valid then append it to the list
                                words.append(s[i+2:i+3])
                                # remove the word from the string
                                s = s[:i+1] + s[i+3:]
    return words