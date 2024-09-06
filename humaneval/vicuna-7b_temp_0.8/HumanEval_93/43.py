
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
    message = message.upper()
    encoded_message = []
    for char in message:
        if char.isalpha():
            if char.islower():
                encoded_char = chr((ord(char) - 32) + 25)
            else:
                encoded_char = chr((ord(char) - 65) + 25)
            encoded_message.append(encoded_char)
        else:
            encoded_message.append(char)
    return encoded_message

print(encode('hello world')) # 'EHBN WORLD'
print(encode('This is a message')) # 'tHKS KS C MGSSCGG'