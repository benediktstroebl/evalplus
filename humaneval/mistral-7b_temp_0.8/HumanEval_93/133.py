
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
    #  replace vowels in the message with the letter that appears 2 places ahead of that 
    #  vowel in the english alphabet. 
    vowels = "aeiou"
    vowel_to_next = {
        'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w'
    }
    message = [c for c in message.upper()]

    def replace_vowels(c):
        if c in vowels:
            return vowel_to_next[c]
        else:
            return c

    message = list(map(replace_vowels, message))
    #  swaps case of all letters
    return ''.join(c.lower() if c.isupper() else c.upper() for c in message)
