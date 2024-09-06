
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
    # n is a natural number
    # s is a string
    # n is less than len(s)
    # we can use a sliding window approach, where the window size is 1 less than n
    # for each window, we check whether it contains exactly n consonants
    # if it does, we add the word to the list
    
    # initialize a list to store the words
    words = []
    
    # initialize a variable to store the current window position
    window_pos = 0
    
    # iterate over each character in the string s
    for i in range(0, len(s)):
        # if the current window position is greater than or equal to n
        if window_pos >= n-1:
            # if the current window contains exactly n consonants, add the word
            # to the list and reset the window position
            if s[i].isalpha() and (window_pos-1) % 2 == 0:
                words.append(s[i:i+n])
                window_pos -= n
            else:
                window_pos += 1
        # otherwise, we check the current character and the previous n-1 characters
        else:
            # check the current character
            if s[i].isalpha() and (window_pos-1) % 2 == 0:
                # add the current word to the list
                words.append(s[i:i+n])
                # check if the current window contains exactly n consonants
                if (window_pos-1) % 2 == 0:
                    window_pos -= 1
                else:
                    window_pos += 1
    
    # return the list of words
    return words