
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
    # Define a dictionary to map uppercase letters to lowercase
    uppercase_map = {chr(ord("A") + i): chr(ord(i) + 1) for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                     }
    # Define a dictionary to map vowels to their 2-place position in the english alphabet
    vowels = "AEIOU"
    vowel_map = {i: (i + 2) % 5 for i in vowels}
    # Define a list to store the encoded message
    encoded_message = []
    # Loop through each character in the message
    for char in message:
        # If the character is a vowel, replace it with its 2-place position in the english alphabet
        if char.lower() in vowels:
            encoded_char = uppercase_map[char.lower()]
        # If the character is not a vowel, append it to the encoded message
        else:
            encoded_char = char
        # Append the encoded character to the encoded message
        encoded_message.append(encoded_char)
    return encoded_message