
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
    words = list()
    if not s:
        return words
    
    # loop through s
    for i in range(len(s)):
        # if letter is not a vowel, increase index 
        if (s[i] not in VOWELS):
            index = i
        # else decrement, as a vowel is now at i - 1
        else:
            index = i - 1
        # when we reach end of string, increment i by 1
        if index == len(s) - 1:
            index += 1
        # when we reach end of string, increment i by 1
        elif index == len(s) - 2:
            index += 1
        # otherwise if a word does not contain n consonants
        if (not is_consonant(s[index], n)):
            continue
        # add word to the list, as index moves right
        words.append(s[index])
    
    return words


"""PART 2 - CHARACTER ANALYSIS"""
