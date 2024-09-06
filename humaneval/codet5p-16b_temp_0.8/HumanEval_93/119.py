
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

    vowels = "AEIOU"
    vowels_indices = []
    new_message = []
    new_message_len = 0
    for letter in message:
        if letter.upper() in vowels:
            vowels_indices.append(new_message_len)
            new_message.append(letter.upper())
        else:
            new_message.append(letter)
        new_message_len += 1

    new_message = [letter for index, letter in enumerate(new_message) if index not in vowels_indices]
    new_message = "".join(new_message)
    
    for index, letter in enumerate(new_message):
        if letter.upper() in vowels:
            new_index = vowels.index(letter.upper()) + 2
            new_letter = vowels[new_index]
            new_message = new_message[:index] + new_letter + new_message[index+1:]
    
    return new_message
