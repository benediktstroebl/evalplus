
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
    # TODO: Replace this line with your solution
    for letter in message:
        if letter.islower():
            letter = letter.upper()
        elif letter.isupper():
            letter = letter.lower()
        else:
            continue
        vowels = 'aeiou'
        if letter in vowels:
            letter = vowels[(vowels.index(letter)+2)%5]
        print(letter, end='')
