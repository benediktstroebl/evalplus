
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
    # Start with an empty list
    words = []
    
    # Iterate over the characters of the string s
    for char in s:
        # If the current character is a letter, continue with the next iteration
        if char.isalpha():
            continue
        
        # If the current character is a space, check the next character
        if char == " ":
            if s[s.find(char)+1].isalpha():
                words.append(s[s.find(char)+1])
            else:
                words.append(s[s.find(char)+1].lower())
                break
        # If the current character is not a space, check the next n-1 characters
        else:
            for i in range(n-1):
                if s[i+1].isalpha():
                    words.append(s[i+1])
                    break
        break
    
    return words
