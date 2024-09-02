
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
    # your code here
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for letter in message:
        result += letter.upper() if letter.islower() else letter.lower()
    for index, letter in enumerate(result):
        if letter in lower_case:
            result = result.replace(letter, lower_case[index+2])
        if letter in upper_case:
            result = result.replace(letter, upper_case[index+2])
    return result
