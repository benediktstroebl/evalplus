
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

    swapped_message = message.swapcase() #case swapped message
    vowel_replaced_message = '' #empty string for vowel replaced message
    for letter in swapped_message:
        if letter in 'AEIOUaeiou':
            vowel_replaced_message += chr(ord(letter)+2) #use ord to convert character to unicode and use the + 2 to get the 2 places ahead
        else:
            vowel_replaced_message += letter
    return vowel_replaced_message

