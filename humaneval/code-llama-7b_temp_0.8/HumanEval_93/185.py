
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

    # Replace all vowels with the letter 2 places ahead of that vowel in the alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_message = ""
    for letter in message:
        if letter in alphabet:
            if letter in "aeiou":
                new_message += alphabet[(alphabet.index(letter) + 2) % len(alphabet)]
            else:
                new_message += letter
        else:
            new_message += letter

    # Replace all letters with the opposite case
    return new_message.swapcase()

