
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
    # Define a dictionary mapping all letters to their lowercase version
    dict_ = {i: i.lower() for i in 'abcdefghijklmnopqrstuvwxyz'}
    
    # Define a dictionary mapping all vowels to their positions in the english alphabet
    pos_dict_ = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    
    # Encode the message by using the above dictionaries
    encoded = []
    for letter in message:
        # Swap the case of the letter
        encoded.append(dict_[letter.upper()])
        
        # Replace the vowel with the letter 2 places ahead of it
        pos = pos_dict_[letter]
        if pos >= 4:
            pos -= 4
        else:
            pos += 2
        encoded.append(pos_dict_[pos])
    return encoded
