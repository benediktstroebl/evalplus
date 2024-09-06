
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
    result = ''

    # For each letter in the message
    for char in message:

        # Lowercase it
        char = char.lower()

        # If it's a vowel
        if char in 'aeiou':
            # Calculate the next letter of the alphabet
            # by adding two to the position of the vowel
            next_letter = chr(ord(char) + 2)

            # Make sure it's upper case
            next_letter = next_letter.upper()

            # Replace the vowel with the next letter
            char = next_letter

        # Uppercase the letter
        char = char.upper()

        # Add it to the result
        result += char

    return result
