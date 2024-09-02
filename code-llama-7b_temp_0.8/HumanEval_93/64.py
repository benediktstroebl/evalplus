
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
    new_message = []
    for letter in message:
        if letter.islower():
            new_message.append(letter.upper())
        else:
            new_message.append(letter.lower())
    for i in range(len(new_message)):
        if new_message[i] in 'aeiou':
            if new_message[i] == 'a':
                new_message[i] = 'c'
            elif new_message[i] == 'e':
                new_message[i] = 'g'
            elif new_message[i] == 'i':
                new_message[i] = 'k'
            elif new_message[i] == 'o':
                new_message[i] = 'p'
            else:
                new_message[i] = 't'
    return ''.join(new_message)

