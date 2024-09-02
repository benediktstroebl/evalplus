
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
    return ''.join(
        ''.join(
            chr(((ord(letter) - ord('a') + number) % 26) + ord('a'))
            if letter.lower() in 'aeiou' else letter
            for letter in word
        )
        for word, number in zip(message.split(), cycle(range(2)))
    )

