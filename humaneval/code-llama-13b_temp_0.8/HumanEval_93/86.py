
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
        if letter in vowels:
            index = vowels.index(letter) + 2
            if index >= len(vowels):
                index = index - len(vowels)
            encoded_message += vowels[index]
        elif letter.isupper():
            index = ord(letter) - 65
            index = (index + 2) % 26
            encoded_message += chr(65 + index)
        else:
            index = ord(letter) - 97
            index = (index + 2) % 26
            encoded_message += chr(97 + index)
    return encoded_message
