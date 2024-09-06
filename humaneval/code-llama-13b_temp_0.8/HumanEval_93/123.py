
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
    result = ''
    vowels = ['a','e','i','o','u']
    for char in message:
        result += caseSwap(char)
        if caseSwap(char).lower() in vowels:
            vowelIndex = vowels.index(caseSwap(char).lower()) + 2
            if vowelIndex > 4:
                vowelIndex -= 5
            result += vowels[vowelIndex]
    return result
