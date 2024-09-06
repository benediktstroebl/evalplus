
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
    new_message = ''
    vowels = 'aeiou'
    vowel_dict = {}
    for i in range(len(vowels)):
        vowel_dict[vowels[i]] = chr(ord(vowels[i]) + 2)

    for letter in message:
        if letter.isalpha():
            new_message += letter.upper() if letter.isupper() else letter.lower()
        else:
            new_message += letter

    for letter in new_message:
        if letter in vowel_dict:
            new_message = new_message.replace(letter, vowel_dict[letter])
    return new_message
