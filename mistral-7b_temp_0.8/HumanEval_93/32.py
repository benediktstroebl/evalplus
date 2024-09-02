
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
    vowels = "AEIOU"
    swap = True
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                letter = chr(ord(letter) + 3)
            else:
                if swap:
                    letter = letter.swapcase()
                    swap = False
                else:
                    swap = True
        print(letter, end = "")

