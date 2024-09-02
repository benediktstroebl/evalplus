
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
    def encode_helper(msg):
        letters = [char for char in msg]
        i = 0
        while i < len(letters):
            if letters[i].lower() in "aeiou":
                letters[i] = chr(ord(letters[i]) + 2)
            i += 1
        return "".join(letters)
    return encode_helper(message)
