
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
    # Encode
    new_message = ''
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowels_found = []
    consonants_found = []
    for letter in message:
        if letter in vowels:
            vowels_found.append(letter)
    vowels_found.sort()
    for letter in vowels_found:
        index = vowels.index(letter)
        new_message += vowels[(index+2)%len(vowels)]
    for letter in message:
        if letter in consonants:
            consonants_found.append(letter)
    consonants_found.sort()
    for letter in consonants_found:
        index = consonants.index(letter)
        new_message += consonants[(index+2)%len(consonants)]
    return new_message
