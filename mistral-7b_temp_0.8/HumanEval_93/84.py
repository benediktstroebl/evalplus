
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
    # Convert the message to lowercase
    message = message.lower()

    # Declare a list for the encoded message and another one for the 
    # vowels
    vowels = 'aeiou'
    encoded_message = []

    # Iterate through each letter in the message
    for letter in message:
        # If the letter is a vowel
        if letter in vowels:
            # Find the index of the vowel in the vowels list
            vowel_index = vowels.index(letter)
            # Add the next vowel to the encoded message
            encoded_message.append(vowels[vowel_index + 2])
        else:
            # Add the letter to the encoded message
            encoded_message.append(letter)

    # Join the letters in the encoded_message list and return the result
    return ''.join(encoded_message)
