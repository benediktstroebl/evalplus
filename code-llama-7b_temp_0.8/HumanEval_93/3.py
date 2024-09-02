
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
    alpha = list(range(97, 123))
    for idx, char in enumerate(alpha):
        if char in message:
            char_idx = alpha.index(char)
            if char_idx == len(alpha) - 1:
                alpha.append(alpha[0])
                encoded_message += alpha[char_idx + 2]
            else:
                encoded_message += alpha[char_idx + 2]

        if char.isupper():
            encoded_message += char.lower()
        elif char.islower():
            encoded_message += char.upper()

    return encoded_message

