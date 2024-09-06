
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
    ##############
    # ALGORITHM #
    ##############
    # 1. create a list of vowels and consonants
    # 2. replace the vowels in the message with the letter that appears 
    #    2 places ahead of the vowel in the english alphabet
    # 3. replace the consonants with their lower case equivalent
    # 4. return the encoded message

    # 1. create a list of vowels and consonants
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    # 2. replace the vowels in the message with the letter that appears 
    #    2 places ahead of the vowel in the english alphabet
    # 3. replace the consonants with their lower case equivalent
    new_message = ''
    for char in message:
        if char in vowels:
            index = vowels.find(char)
            new_message += vowels[index - 2]
        elif char in consonants:
            new_message += char.lower()
        else:
            new_message += char
    return new_message

