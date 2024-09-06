
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
    message = message.lower()
    message_encode = ""
    vowels = ['a','e','i','o','u']
    for letter in message:
        if letter in vowels:
            vowel_index = vowels.index(letter)
            if vowel_index == 4:
                new_letter = vowels[2]
            else:
                new_letter = vowels[vowel_index + 2]
            message_encode += new_letter.upper()
        else:
            message_encode += letter.upper()
    return message_encode
    
