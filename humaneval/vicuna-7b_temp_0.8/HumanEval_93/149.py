
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
    # Create a dictionary of the English alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Create a dictionary of the numbers of letters between the vowels
    vowel_dict = {
        "a": 2, "e": 2, "i": 2, "o": 2, "u": 2, "y": 2
    }
    # Encode the message
    encoded_message = ""
    for char in message:
        # If the char is a vowel, replace it with the number of letters ahead
        if char.lower() in vowel_dict:
            new_char = str(vowel_dict[char.lower()] + 2)
        # If the char is not a vowel, replace it with the corresponding number
        else:
            new_char = str(ord(char) + 1)
        # Append the encoded char to the encoded message
        encoded_message += new_char
    return encoded_message
