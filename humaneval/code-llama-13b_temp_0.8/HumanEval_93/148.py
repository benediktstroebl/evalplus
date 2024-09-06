
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
    encoded = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                encoded += letter.lower()
            else:
                encoded += letter.upper()
        else:
            encoded += letter

    for idx, letter in enumerate(encoded):
        if letter in vowels:
            try:
                encoded = encoded[:idx] + chr(ord(letter)+2) + encoded[idx+1:]
            except:
                # wrap around to a
                encoded = encoded[:idx] + 'a' + encoded[idx+1:]

    return encoded
