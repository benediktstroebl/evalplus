
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
    #your code goes here
    msg = message.lower()
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for char in msg:
        if char in alphabet:
            answer += alphabet[alphabet.index(char) ^ 1]
        elif char == ' ':
            answer += ' '
        elif char in vowels:
            answer += alphabet[(alphabet.index(char) + 2) % 26]
        else:
            answer += char
    return answer

