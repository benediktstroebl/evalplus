
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
    # Your code here
    encoded = []
    for letter in message:
        # swap case
        if letter.islower():
            letter = letter.upper()
        else:
            letter = letter.lower()
        # replace vowels
        if letter in "AEIOU":
            # replace with the letter 2 places ahead of the vowel
            letter = chr(ord(letter) + 2)

        encoded.append(letter)

    return "".join(encoded)

