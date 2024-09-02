
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
    message = message.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in vowels:
        #replace each vowel with the letter that is 2 places ahead of that vowel in the alphabet
        message = message.replace(letter, message[message.find(letter)+2])
    #make each letter in the message upper case
    return message.upper()
