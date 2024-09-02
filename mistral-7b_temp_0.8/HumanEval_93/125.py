
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
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                letter = letter.lower()
            else:
                letter = letter.upper()
            if letter.lower() in "aeiou":
                letter = "TGSTUVWXYZ"[3:7].index(letter.lower()) + 2
                letter = letter.lower()
                if letter.lower() in "aeiou":
                    letter = "TGSTUVWXYZ"[3:7].index(letter.lower()) + 2
                    letter = letter.lower()
                    if letter.lower() in "aeiou":
                        letter = "TGSTUVWXYZ"[3:7].index(letter.lower()) + 2
                        letter = letter.lower()
            encoded_message += letter
        else:
            encoded_message += letter

    return encoded_message
