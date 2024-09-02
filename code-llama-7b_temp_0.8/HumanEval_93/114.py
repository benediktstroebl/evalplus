
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
    # Two ways of doing this
    # 1
    # new_str = ''
    # for letter in message:
    #     if letter.isalpha():
    #         if letter.isupper():
    #             new_str += letter.lower()
    #         else:
    #             new_str += letter.upper()
    #     else:
    #         new_str += letter
    #     if letter.lower() in 'aeiouy':
    #         index = 'aeiouy'.find(letter.lower()) + 2
    #         if index >= 'aeiouy'.length:
    #             index = index - 'aeiouy'.length
    #         new_str += 'aeiouy'[index]
    # return new_str

    # 2
    # new_str = ''
    # for letter in message:
    #     if letter.lower() in 'aeiouy':
    #         index = 'aeiouy'.find(letter.lower()) + 2
    #         if index >= 'aeiouy'.length:
    #             index = index - 'aeiouy'.length
    #         new_str += 'aeiouy'[index]
    #     else:
    #         new_str += letter
    #     if letter.isupper():
    #         new_str += letter.lower()
    #     else:
    #         new_str += letter.upper()
    # return new_str

    # 3
    new_str = ''
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                new_str += letter.lower()
            else:
                new_str += letter.upper()
            if letter.lower() in 'aeiouy':
                index = 'aeiouy'.find(letter.lower()) + 2
                if index >= 'aeiouy'.length:
                    index = index - 'aeiouy'.length
                new_str += 'aeiouy'[index]
        else:
            new_str += letter
    return new_str

