
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
    encoded = []
    for i in range(len(message)):
        for j in range(len(message) - i - 1):
            if message[j] == 'a' or message[j] == 'e' or message[j] == 'i' or message[j] == 'o' or message[j] == 'u':
                index = j + 2
                if index < len(message):
                    encoded.append(chr(ord('a') + index - 1))
                    encoded.append(chr(ord(message[j]) - index))
                    encoded.append(chr(ord(message[j + 1]) + index))
                    encoded.append(chr(ord(message[j + 2]) - index))
                    encoded.append(chr(ord(message[j + 3]) + index - 1))
            else:
                encoded.append(chr(ord(message[j])))
        encoded.append(chr(ord('a') + len(message) - 1))
    return encoded[::-1]
