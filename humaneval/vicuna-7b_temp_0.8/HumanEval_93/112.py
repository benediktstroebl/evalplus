
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
    # Convert the message to a list of characters
    message_list = list(message)

    # Reverse the list of characters so that uppercase letters become lowercase
    message_list.reverse()

    # Create a dictionary that maps each vowel to the letter that appears 2 places ahead of that vowel in the english alphabet
    vowel_mapping = {
        'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'
    }

    # Iterate through each character in the message
    for i, char in enumerate(message_list):
        # If the character is a vowel, replace it with the corresponding vowel in the vowel mapping
        if char.isupper():
            char = vowel_mapping[char]

        # Otherwise, leave the character as is
        else:
            pass

        # Append the encoded character to the result string
        result_string += char

    return ''.join(result_string)