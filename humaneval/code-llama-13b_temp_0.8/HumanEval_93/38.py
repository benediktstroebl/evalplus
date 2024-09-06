
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
    vowels = ('a', 'e', 'i', 'o', 'u')
    # new_message = ''
    # for letter in message:
    #     if letter in vowels:
    #         idx = vowels.index(letter)
    #         new_letter = vowels[idx+2]
    #         if new_letter in vowels:
    #             new_letter = new_letter.upper()
    #         new_message += new_letter
    #     else:
    #         new_message += letter.lower()
    # return new_message
    # use list comprehension:
    return ''.join([letter.lower() if letter.lower() not in vowels else
                    vowels[(vowels.index(letter.lower())+2) % len(vowels)]
                    if letter.islower()
                    else vowels[(vowels.index(letter.lower())+2) % len(vowels)]
                    for letter in message])
    # return ''.join([letter.lower() if letter.lower() not in vowels
    #                 else vowels[(vowels.index(letter.lower())+2) % len(vowels)]
    #                 if letter.islower()
    #                 else vowels[(vowels.index(letter.lower())+2) % len(vowels)]
    #                 for letter in message])
    
