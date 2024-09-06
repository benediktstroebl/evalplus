
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

    
    message_lowercase = message.lower()
    vowels = ['a','e','i','o','u']
    letters = [letter for letter in message_lowercase]
    new_letters = []
    
    for i in range(0,len(letters)):
        if letters[i] in vowels:
            new_letters.append(letters[i+2])
            i += 2
        else:
            new_letters.append(letters[i])
            i += 1
    
    return ''.join(new_letters)

