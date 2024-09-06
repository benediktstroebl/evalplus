
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
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet.split(alphabet)
    message = "".join(sorted(alphabet))
    for letter in message:
        if letter in "aeiouAEIOU":
            place = 2
            while place < len(alphabet) and alphabet[place] == letter:
                place += 2
            if place < len(alphabet):
                message = message[:letter] + alphabet[place] + message[letter+1:]
    return message