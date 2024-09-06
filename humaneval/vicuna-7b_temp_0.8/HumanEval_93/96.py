
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
    def encode_word(word):
        # swap case
        word = word.upper()
        # replace 'e' with '3', 'i' with '2', 'o' with '9', 'a' with '5', 'u' with '7'
        word = word.replace('e', '3')
        word = word.replace('i', '2')
        word = word.replace('o', '9')
        word = word.replace('a', '5')
        word = word.replace('u', '7')
        return word
    
    message = message.lower()
    return ''.join([encode_word(word) for word in message])