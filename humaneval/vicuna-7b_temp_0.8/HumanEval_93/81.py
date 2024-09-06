
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
    message = message.upper()
    # create a string from the message
    message_str = ''.join(message)
    # use a dictionary to map each vowel to its position in the alphabet
    vowel_map = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    # use a while loop to iterate through the characters in the message_str
    result = ''
    index = 0
    while index < len(message_str):
        # check if the current character is a vowel
        if message_str[index] in vowel_map:
            # get the position of the vowel in the alphabet
            vowel_pos = vowel_map[message_str[index]]
            # get the character 2 places ahead of the vowel in the alphabet
            next_char = ''.join([chr(ord('a') + i) for i in range(vowel_pos, vowel_pos + 2)])
            # replace the vowel with the next character
            result += next_char + message_str[index+1]
        else:
            # add the character to the result
            result += message_str[index]
        # increment the index
        index += 1
    return result