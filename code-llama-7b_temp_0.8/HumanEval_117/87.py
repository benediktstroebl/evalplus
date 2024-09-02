
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

    """
    Plan:
    - for loop, iterate through each word
    - check if the word contains more than n consonants
    - append to list if it does
    """
    # create a list to hold the words with at least n consonants
    lst = []

    # split the string into a list of words
    s_list = s.split(" ")
    # print(s_list)

    # for loop that iterates through the list
    for word in s_list:
        # create a list to hold the consonants
        cons_lst = []
        # for loop that iterates through the word
        for char in word:
            # if char is in consonants set, append to cons_lst
            if char in consonants:
                cons_lst.append(char)
        # if length of cons_lst is equal to n, add word to list
        if len(cons_lst) == n:
            lst.append(word)
    return lst


