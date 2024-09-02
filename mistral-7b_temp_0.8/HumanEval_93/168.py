
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
    ans = ""
    lower = []
    upper = []
    vowels = "aeiou"
    for i in message:
        if i.islower():
            lower.append(i)
        if i.isupper():
            upper.append(i)

    for i in range(0,len(lower)):
        if lower[i] in vowels:
            ans = ans + lower[i-2]
        else:
            ans = ans + lower[i]

    for i in range(0,len(upper)):
        if upper[i] in vowels:
            ans = ans + upper[i-2]
        else:
            ans = ans + upper[i]

    return ans
