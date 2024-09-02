
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
    vowels = 'aeiou'
    vowel_pos = [vowels.index(x) for x in vowels]
    map = {}
    map.update((v, vowel_pos[vowels.index(v)]+2) for v in vowels)
    encode_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encode_message += chr(ord(char.upper()))
            else:
                encode_message += chr(ord(char.lower()))
        else:
            encode_message += char
    encode_message = encode_message.lower()
    for char in encode_message:
        if char in map:
            encode_message = encode_message.replace(char, chr(ord('a') + map[char]))
    return encode_message
