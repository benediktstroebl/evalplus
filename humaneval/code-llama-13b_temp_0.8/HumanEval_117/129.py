
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
    # create a list to store the words containing n consonants
    words = []
    # list of consonants
    cons = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    # split the string to a list of words
    word_list = s.split()
    # check if each word contains n consonants only and if yes, append to words list
    for word in word_list:
        if word.lower() != word.upper():
            count = 0
            for char in word.lower():
                if char in cons:
                    count += 1
            if count == n:
                words.append(word)
    return words
    
    
