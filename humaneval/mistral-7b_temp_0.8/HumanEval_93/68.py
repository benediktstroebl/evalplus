
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
    #translate message to upper case and replace vowels with the letters that appear 
    # 2 positions ahead of the vowel
    newMessage = message.upper()
    for i in "AEIOU":
        newMessage = newMessage.replace(i, chr(ord(i)+2))
    #swap the case of the letters
    newMessage = newMessage.swapcase()
    return newMessage
    #return message
