
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
    encoded = []
    vowels = "aeiouAEIOU"
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                index = (vowels.index(letter) + 2) % 10
                encoded.append(vowels[index])
            else:
                encoded.append(letter.swapcase())
        else:
            encoded.append(letter)
    return ''.join(encoded)
            
