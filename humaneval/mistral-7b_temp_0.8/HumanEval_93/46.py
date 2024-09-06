
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
    # C - 69 	 A - 65 	 Z - 90
    # a - 97 	 z - 122
    # 26 letters in the alphabet
    # 25 letters between a and z
    # case swap and vowel swap
    # islower and isupper

    # temp variables
    message = message.lower()
    # encoded_message = ''
    # index = 0
    # while index < len(message):
    #     # temp_char = message[index]
    #     # if 'a' <= temp_char <= 'z':
    #     #     if temp_char == 'a':
    #     #         temp_char = 'c'
    #     #     elif temp_char == 'e':
    #     #         temp_char = 'g'
    #     #     elif temp_char == 'i':
    #     #         temp_char = 'k'
    #     #     elif temp_char == 'o':
    #     #         temp_char = 'q'
    
