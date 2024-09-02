
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

    #make lower case
    encoded_message = message.lower()

    #look for vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    #cycle through encoded_message and swap cases
    for i, char in enumerate(encoded_message):
        if char in vowels:
            #find index of char in vowels
            index = vowels.index(char)

            #find the char 2 places ahead of it in vowels
            #then add it to the new message
            encoded_message = encoded_message[:i] + vowels[index + 2] + encoded_message[i + 1:]

    return encoded_message
