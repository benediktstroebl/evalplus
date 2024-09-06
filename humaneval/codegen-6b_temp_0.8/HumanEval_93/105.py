
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
    
    #place to save the encoded message. 
    encoded_message = ''
    
    #convert the message to lowercase
    low_message = message.lower()
    
    #place to save the encoded message. 
    encoded_message = ''
    
    #dict of all the letters in the english alphabet. 
    letters = {
        'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 
        'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5', 
        'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 
        's': '7', 't': '7', 'u': '7', 'v': '7', 'w': '9', 'x': '9', 
        'y': '9', 'z': '9', 
        'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3', 
        'G': '4', 'H': '4', 'I': '4', 'J': '5', 'K': '5', 'L': '5', 
        'M': '6', 'N': '6', 'O': '6', 'P': '7', 'Q': '7', 'R': '7', 
        'S': '7', 'T': '7', 'U': '7', 'V': '7', 'W': '9', 'X': '9', 
        'Y': '9', 'Z': '9',
        ' ': '0',
        '~': '~', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', 
        '^': '^', '&': '&', '*': '*', '(': '(', ')': ')', '-': '-', 
        '=':