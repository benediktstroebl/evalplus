
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
    # Iterate through each character in the string s
    for i, c in enumerate(s):
        # Initialize an empty list to store the words
        words = []
        
        # Check if the current character c is a consonant
        if c.isalpha() and c.isalpha():
            # If the current character c is a consonant, append it to the list words
            words.append(c)
        
        # If the current character c is a space, append all the words in the list words to the output list
        elif i == len(s) - 1 and s[i-1].isalpha() and s[i-1].isalpha():
            words.extend(words)
            break
        
        # If the current character c is a vowel, skip it
        elif not c.isalpha() or not c.isalpha():
            continue
        
        # If the current word is the desired length, append it to the output list
        elif len(words) == n:
            words.append("".join(words))
            break
        
        # If the current word is not the desired length, append the remaining characters to the output list
        else:
            words.append(c)
        
        # If the current word is not the desired length, append the remaining words to the output list
        else:
            words.append(words)
            
        # If the current word is not the desired length, append the remaining words to the output list
        break
    
    return words
