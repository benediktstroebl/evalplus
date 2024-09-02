
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
    encoded_message = []
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded_message.append(letter.upper())
            elif letter.isupper():
                encoded_message.append(letter.lower())
            else:
                encoded_message.append(letter)
        else:
            encoded_message.append(letter)
    
    encoded_message2 = []
    for i in range(len(encoded_message)):
        if encoded_message[i] in ['a', 'e', 'i', 'o', 'u', 'y']:
            if i + 2 > len(encoded_message) - 1:
                encoded_message2.append(encoded_message[i])
            else:
                encoded_message2.append(encoded_message[i + 2])
        else:
            encoded_message2.append(encoded_message[i])

    return ''.join(encoded_message2)

