
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
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            index = ord(letter) - 2
            if index >= "A":
                index += 26
            elif index >= "B":
                index += 22
            elif index >= "C":
                index += 18
            elif index >= "D":
                index += 14
            elif index >= "E":
                index += 12
            else:
                index += 6
            encoded_message += chr(index)
        else:
            encoded_message += letter
    return encoded_message
