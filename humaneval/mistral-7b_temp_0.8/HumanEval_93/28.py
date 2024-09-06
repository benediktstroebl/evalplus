
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
    encode_result = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                char = char.upper()
                encode_result += char
            else:
                char = char.lower()
                encode_result += char
        else:
            encode_result += char
    vowels = 'aeiou'
    for i in range(len(message)):
        if message[i] in vowels:
            encode_result = encode_result[:i] + chr(ord(message[i]) + 2) + encode_result[i + 1:]
    return encode_result
    # return encode_result.replace('a', 'b').replace('e', 'd').replace('i', 'h').replace('o', 'g').replace('u', 'f')
    # return encode_result.replace('a', 'b').replace('e', 'c').replace('i', 'd').replace('o', 'e').replace('u', 'f')
    # return encode_result.replace('a', 'b').replace
