
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
    
    output = []
    for char in message:
        if char.isalpha():
            # Make sure we have a capital
            if char.islower():
                char = char.upper()
            # Get the location of the char in the alphabet
            location = ord(char) - ord('A')
            # Get the new letter
            new_letter = chr(((location + 2) % 26) + ord('A'))
            if char.islower():
                new_letter = new_letter.lower()
            output.append(new_letter)
        else:
            output.append(char)
    return ''.join(output)
