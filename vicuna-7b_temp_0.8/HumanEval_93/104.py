
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
    # change all letters to lowercase
    message = message.lower()
    
    # iterate through the message
    for char in message:
        # if the char is a vowel, change it to the next letter in the english alphabet
        if char.isalpha():
            if char.lower() in 'aeiou':
                # if the char is a vowel, change it to the next letter in the english alphabet
                char = chr(ord(char) + 2)
            else:
                # if the char is not a vowel, do nothing
                pass
        else:
            # if the char is not a vowel, do nothing
            pass
        
        # append the char to the encoded string
        encoded_string += char
    
    # return the encoded string
    return encoded_string
