
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
    encoded_message = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                letter_index = (ord(letter) + 2 - ord('a')) % 26 + ord('a')
                encoded_message += chr(letter_index)
            else:
                encoded_message += letter.upper() if letter.islower() else letter.lower()
        else:
            encoded_message += letter
    return encoded_message
