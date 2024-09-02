
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
    vowels = set('aeiouAEIOU')
    
    def replace(match):
        if match.group(0) in vowels:
            return chr(ord(match.group(0)) + 2)
        return match.group(0)
    
    message = message.lower()
    return re.sub(r'[aeiou]+', replace, message)
