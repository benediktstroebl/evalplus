
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
    # Step 1: check if string is empty
    # if s == "":
    #     return []
    
    # Step 2: check if n is less than or equal to 0
    # if n <= 0:
    #     return []
    
    # Step 3: make list of all words in string s
    # make list of words
    word_list = s.split(" ")
    
    # Step 4: loop over each word
    # list of words with n consonants
    list_with_n = []
    for word in word_list:
        # Step 5: check if there are more than one character
        # if there are more than one character
        if len(word) > 1:
            # Step 6: check if word has n consonants
            # count of consonants
            count_consonants = 0
            # loop over each character
            for character in word:
                # if character is not a letter
                if character.isalpha() == False:
                    # add 1 to count of consonants
                    count_consonants += 1
            # if count of consonants is equal to n
            if count_consonants == n:
                # add word to list of words with n consonants
                list_with_n.append(word)
    
    # Step 7: return list of words with n consonants
    return list_with_n
