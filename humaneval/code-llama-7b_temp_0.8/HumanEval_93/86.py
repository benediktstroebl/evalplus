
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
    # Step 1: Convert message into lowercase letters
    message = message.lower()
    # Step 2: Initialize encoded_message as ''
    encoded_message = ''
    # Step 3: Iterate through message
    for char in message:
        # Step 4: If char is in vowels, use string.ascii_lowercase to find the 2 places ahead of it.
        # Step 5: Replace char with the letter that appears 2 places ahead of that vowel in the english alphabet.
        if char in 'aeiou':
            vowels_pos = 'aeiou'.index(char)
            replace_char = 'aeiou'.find('aeiou', vowels_pos + 2)
            char = 'aeiou'[replace_char]
        # Step 6: Append char to encoded_message
        encoded_message += char
    # Step 7: return encoded_message
    return encoded_message
    
