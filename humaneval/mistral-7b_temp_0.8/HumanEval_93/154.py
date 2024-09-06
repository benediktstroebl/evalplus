
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

    # create an empty string
    encoded_string = ""

    # for loop for going through each letter in the message
    for letter in message:

        # if letter is a vowel
        if letter in "aeiou":
            # add to encoded_string
            encoded_string += chr(ord(letter) + 2)

        # if letter is not a vowel
        else:
            # add to encoded_string
            encoded_string += letter.upper() if letter.islower() else letter.lower()

    # return the encoded_string
    return encoded_string



