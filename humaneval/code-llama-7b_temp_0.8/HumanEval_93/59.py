
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
    
    # creating the vowels string
    vowels = 'aeiou'
    
    # Creating the output string
    output = ''
    
    # Looping through each character in the message
    for c in message:
        # check if the character is a vowel
        if c in vowels:
            # If it is a vowel, determine which index it is and
            # add the character in the output string that is 2 places ahead of that vowel in the alphabet
            output += message[message.find(c) + 2]
        else:
            # If it is not a vowel, use the upper function to make it uppercase
            output += c.upper()
    
    # Return the output string
    return output

