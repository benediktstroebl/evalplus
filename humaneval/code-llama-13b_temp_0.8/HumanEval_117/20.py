
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
    # PLAN
    # make a list of all the consonants
    # make a counter
    # iterate through string
    # if index is not a space and is in consonant list, add to counter
    # if index is a space, check counter, if it equals the value of n, add the word to a list
    # return the list
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    count = 0
    answer_list = []
    for i in range(len(s)):
        if s[i] not in consonants:
            continue
        elif s[i] in consonants:
            count += 1
        if s[i] == ' ':
            if count == n:
                answer_list.append(s[i-n:i])
                count = 0
    return answer_list

