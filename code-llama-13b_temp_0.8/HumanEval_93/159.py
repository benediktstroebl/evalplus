
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
    
    # create a mapping of letters and corresponding numbers
    letter_numbers = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26
    }
    
    # create a mapping of numbers and corresponding letters
    number_letters = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
        6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
        11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
        16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
        21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
        26: 'z'
    }
    
    # create mapping of vowels and numbers two ahead of them
    vowel_numbers = {
        'a': 3, 'e': 5, 'i': 7, 'o': 9, 'u': 11
    }
    
    # encode message
    encoded_message = ''
    for letter in message:
        if letter.islower():
            encoded_message += number_letters[letter_numbers
