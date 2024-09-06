
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
    result = ""
    for letter in message:
        if letter.isupper():
            result += letter.lower()
        elif letter.islower():
            result += letter.upper()
        else:
            result += letter
    result2 = ""
    for letter in result:
        if letter in "aeiou":
            index = "aeiou".find(letter) + 2
            if index >= 5:
                index -= 5
            result2 += "AEIOU"[index]
        else:
            result2 += letter
    return result2
