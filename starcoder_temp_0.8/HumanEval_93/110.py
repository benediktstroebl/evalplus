
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
    
    vowels = ["a", "e", "i", "o", "u"]
    
    newMessage = ""
    for letter in message:
        if letter in vowels:
            if letter.isupper():
                newMessage += vowels[(vowels.index(letter.lower())+2)%5].upper()
            else:
                newMessage += vowels[(vowels.index(letter)+2)%5]
        else:
            if letter.isupper():
                newMessage += letter.lower()
            else:
                newMessage += letter
    return newMessage
