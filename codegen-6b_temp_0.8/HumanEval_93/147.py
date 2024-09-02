
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
    encoded = ""
    for word in message.split(" "):
        new_word = ""
        for letter in word.lower():
            if letter in ["a", "e", "i", "o", "u"]:
                new_word += letter + chr(ord(letter) - 1)
            else:
                new_word += letter
        encoded += new_word + " "
    return encoded[:-1]
