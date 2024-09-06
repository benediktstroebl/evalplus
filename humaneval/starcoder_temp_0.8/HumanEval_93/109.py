
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
    
    encoded_message = []
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for letter in message:
        if letter.lower() in vowel_list:
            position = vowel_list.index(letter.lower())
            if position == 0:
                encoded_message.append(vowel_list[1])
            else:
                encoded_message.append(vowel_list[position - 2])
        else:
            encoded_message.append(letter)
    return ''.join(encoded_message)
