
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
    # Create a list to store the selected words
    selected_words = []
    
    # Create an empty list to store the indexes of consonants
    consonant_indices = []
    
    # Set the current index to 0
    current_index = 0
    
    # Loop through the characters in the string
    for char in s:
        # If the current character is a consonant
        if char.isupper():
            # Add the current character to the list of selected words
            selected_words.append(s[current_index:current_index+1])
            
            # Add the current character to the list of consonant indices
            consonant_indices.append(current_index)
        
        # If the current character is a vowel
        elif char.islower():
            # Remove the current character from the string and the list of selected words
            s = s.replace(s[current_index], "", 1)
            selected_words.remove(s[current_index])
            
            # Remove the current character from the list of consonant indices
            consonant_indices.remove(current_index)
        
        # If the current character is a space
        elif char == " ":
            # If the previous character was a consonant
            if current_index-1 >= 0:
                # Add the previous character to the list of selected words
                selected_words.append(s[current_index-1:current_index])
            
            # Add the current character to the list of consonant indices
            consonant_indices.append(current_index)
        
        # Increment the current index by 1
        current_index += 1
        
    # Add the final selected word to the list of selected words
    selected_words.append(s[current_index:])
    
    return selected_words