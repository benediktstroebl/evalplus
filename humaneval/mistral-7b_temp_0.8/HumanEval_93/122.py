
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
    enc_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                enc_char = char.upper()
            else:
                enc_char = char.lower()
            enc_message += enc_char
        else:
            enc_message += char
    vowels = ["a","e","i","o","u"]
    vowel_index = []
    for i, letter in enumerate(message):
        if letter in vowels:
            vowel_index.append(i)
    if len(vowel_index) > 0:
        new_vowels = []
        for i in vowel_index:
            new_vowels.append(message[i+2])
        enc_message = enc_message.replace(message[vowel_index[0]], new_vowels[0])
    return enc_message

