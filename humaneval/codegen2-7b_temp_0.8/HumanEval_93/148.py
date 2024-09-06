
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
    def helper(message, index, output):
        if index == len(message):
            return output
        else:
            if message[index].lower() in vowels:
                output += message[index].lower()
            elif message[index].lower() == message[index].upper():
                output += message[index].lower()
            else:
                output += message[index]
            return helper(message, index+1, output)
    
    return helper(message, 0, ''
