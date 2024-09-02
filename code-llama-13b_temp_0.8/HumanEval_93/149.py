
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
    newMessage = []
    vowels = 'aeiou'
    offset = 2
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                newLetter = letter.lower()
            else:
                newLetter = letter.upper()
            if newLetter in vowels:
                index = (vowels.index(newLetter) + offset) % 5
                newLetter = vowels[index]
        else:
            newLetter = letter
        newMessage.append(newLetter)
    return ''.join(newMessage)
