
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
    #==============================================================================
    # if len(message) > 0:
    #     for i in range(0, len(message)):
    #         if message[i].isalpha():
    #             if message[i] == message[i].lower():
    #                 message[i] = message[i].upper()
    #             elif message[i] == message[i].upper():
    #                 message[i] = message[i].lower()
    #             elif message[i] in 'aeiou':
    #                 if message[i].lower() == 'a':
    #                     message[i] = 'E'
    #                 elif message[i].lower() == 'e':
    #                     message[i] = 'I'
    #                 elif message[i].lower() == 'i':
    #                     message[i] = 'O'
    #                 elif message[i].lower() == 'o':
    #                     message[i] = 'U'
    #                 elif message[i].lower() == 'u':
    #                     message[i] = 'A'
    #             else:
    #                 pass
    #     print(''.join(message))
    #==============================================================================
    vowels = 'aeiouAEIOU'
    def shift(letter):
        if letter not in vowels:
            return letter
        else:
            return vowels[vowels.index(letter) - 2]
    return ''.join(shift(letter) for letter in message)

