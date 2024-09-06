
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
    letters = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = ''
    
    # first, swap case of all letters
    for i in message:
        if i in letters:
            if i == i.upper():
                encoded_message += i.lower()
            else:
                encoded_message += i.upper()
        else:
            encoded_message += i
    
    # second, replace all vowels with the letter 2 places ahead of it
    for i in range(len(encoded_message)):
        if encoded_message[i] in 'aeiou':
            two_letters_ahead = letters[letters.index(encoded_message[i]) + 2]
            encoded_message = encoded_message[:i] + two_letters_ahead + encoded_message[i+1:]
            
    return encoded_message

