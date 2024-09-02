
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    # Create a new string for the output
    output = ""
    
    # Loop through the characters in the message
    for char in message:
        # If the char is a vowel, replace it with its 2-place-ahead 
        # counterpart
        if char.isalpha():
            # Get the index of the vowel
            vowel_index = ALPHABET.index(char)
            
            # Get the index of the 2-place-ahead vowel
            next_vowel_index = vowel_index + 2
            
            # If the next vowel is in the alphabet, replace the char
            if ALPHABET[next_vowel_index].isalpha():
                output += ALPHABET[next_vowel_index]
            else:
                # Replace the char with its 2-place-ahead counterpart
                output += ALPHABET[vowel_index]
        else:
            # If the char is not a vowel, add it directly to the output
            output += char
    
    return output
