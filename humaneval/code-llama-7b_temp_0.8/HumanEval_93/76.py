
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
    
    #this is not the most efficient way of doing this
    #but it's the way I wanted to do it
    #this could be done in one line if I wasn't thinking
    #very hard about how to do it
    
    vowels = 'aeiou'
    message = message.lower()
    encoded_message = ''
    
    for letter in message:
        if letter in vowels:
            index = vowels.find(letter)
            letter = vowels[(index+2)%len(vowels)]
        if letter.isalpha():
            if letter.islower():
                letter = letter.upper()
            else:
                letter = letter.lower()
        encoded_message += letter
    return encoded_message
