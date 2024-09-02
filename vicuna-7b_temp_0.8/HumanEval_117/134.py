
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
    # use a list to keep track of current word
    current_word = []
    # keep track of current position in the string
    current_pos = 0
    
    # loop through the string
    for i in range(1, len(s)):
        # if the current character is a consonant
        if s[i] in 'bcdfghjklmnpqrstvwxyz':
            # if the next word starts with a vowel
            if current_word and s[current_pos] == 'a' or s[current_pos] == 'A':
                # append the current word to the result list
                result.append(current_word)
                # clear the current word
                current_word = []
                # increment the current position
                current_pos += 1
            # add the current character to the current word
            current_word.append(s[i])
        # if the current character is a vowel
        elif s[i] in 'aeiouAEIOU':
            # if the current word is not empty
            if current_word:
                # append the current word to the result list
                result.append(current_word)
                # clear the current word
                current_word = []
            # add the current character to the current word
            current_word.append(s[i])
        # update the current position
        current_pos = i
    
    # if the current word is not empty
    if current_word:
        # append the current word to the result list
        result.append(current_word)
    
    return result