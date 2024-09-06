
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
    # First lets strip the string
    s = s.strip()

    # split the string into a list
    s_list = s.split()

    # create an empty list
    cons_list = []

    # for each word in the list
    for word in s_list:
        # set a counter
        counter = 0

        # for each letter in the word
        for letter in word:
            # if the letter is a consonant
            if letter not in "aeiouAEIOU":
                # increment the counter
                counter += 1

        # if the counter is equal to n
        if counter == n:
            # append it to the list
            cons_list.append(word)

    # return the list
    return cons_list
