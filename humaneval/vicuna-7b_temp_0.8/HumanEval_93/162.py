
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
    # Step 1: Swap case of all letters
    message = ''.join([chr(ord('A') + i) for i in range(len(message))])
    # Step 2: Replace vowels with their vowel neighbors
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(len(message)):
        if message[i] in vowels:
            if i % 2 == 0:
                result.append(vowels[i + 1])
            else:
                result.append(vowels[i - 1])
        else:
            result.append(message[i])
    return ''.join(result)