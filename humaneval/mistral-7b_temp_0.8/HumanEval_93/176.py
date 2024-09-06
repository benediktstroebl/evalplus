
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
    # YOUR CODE HERE
    vowels = 'aeiou'
    new_message = ''
    for i in message:
        if i.isalpha():
            if i.lower() in vowels:
                pos = vowels.find(i.lower())
                if pos > -1:
                    new_message += vowels[pos+2].lower()
                else:
                    new_message += i
            else:
                new_message += i.swapcase()
        else:
            new_message += i
    return new_message

