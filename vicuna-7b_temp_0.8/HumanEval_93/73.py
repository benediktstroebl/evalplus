
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

    # Create a string to store the encoded message
    encoded = ""

    # Iterate through each character in the message
    for char in message:
        # If the character is a vowel, replace it with the next vowel in the alphabet
        if char.lower() in "aeiouAEIOU":
            # Find the position of the current vowel in the alphabet
            vowel_index = "AEIOU".index(char.lower()) + 1

            # Replace the vowel with the letter at the same index in the alphabet
            encoded += chr(vowel_index)
        else:
            # If the character is not a vowel, just append it to the encoded message
            encoded += char

    return encoded