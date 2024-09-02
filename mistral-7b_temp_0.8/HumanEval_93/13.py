
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
        if letter.isalpha():
            if letter.isupper():
                result += letter.lower()
            else:
                result += letter.upper()
        else:
            result += letter
    vowels = 'aeiou'
    for index, letter in enumerate(message):
        if letter.isalpha():
            if letter.lower() in vowels:
                if index + 2 < len(message):
                    result = result[:index] + message[index + 2] + result[index + 2:]
            else:
                result = result[:index] + letter + result[index + 1:]
    return result
