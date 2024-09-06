
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
    # Create a list of characters in the message
    message_chars = list(message)

    # Loop through each character in the message
    for i, char in enumerate(message_chars):
        # If the character is a letter, change it to lowercase
        if char.isalpha():
            message_chars[i] = chr(ord(char) + 32)

    # Loop through each character in the message
    for i, char in enumerate(message_chars):
        # If the character is a vowel, replace it with the 2nd letter in the english alphabet after it
        if char.isalpha() and char.islower():
            temp = chr(ord(char) + 26)
            message_chars[i] = chr(temp + ord('a'))

    return ''.join(message_chars)
