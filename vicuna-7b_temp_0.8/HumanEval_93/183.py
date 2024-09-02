
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
    # Define mapping of letters and their positions in english alphabet
    mapping = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
        'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
        'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
        's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
        'y': 'Y', 'z': 'Z'
    }

    # Define function to swap case of a letter
    def swap_case(letter):
        if letter.isupper():
            return letter.lower()
        else:
            return letter

    # Define function to replace vowel with its 2 place ahead letter
    def replace_vowel(letter):
        if letter.isvowel():
            return mapping[mapping.index(letter) + 2]
        else:
            return letter

    # Encode message
    message = ''.join(swap_case(ord(letter)) for letter in message)
    return message
