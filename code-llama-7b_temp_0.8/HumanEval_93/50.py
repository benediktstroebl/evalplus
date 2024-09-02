
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
    vowels = "aeiou"
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                ind = vowels.index(letter)
                if ind == 4:
                    result += vowels[0]
                else:
                    result += vowels[ind + 2]
            else:
                if letter.islower():
                    result += letter.upper()
                else:
                    result += letter.lower()
        else:
            result += letter
    return result
