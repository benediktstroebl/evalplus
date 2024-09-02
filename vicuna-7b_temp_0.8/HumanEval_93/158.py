
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
    # Create a dictionary of all the vowels in the english alphabet
    vowels = "aeiouAEIOU"
    
    # Create a dictionary of the numbers of the vowels in the english 
    # alphabet, with 2 places ahead counting as 2, 3 places ahead as 3,
    # etc.
    num_vowels = {2: 2, 3: 3, ..., 0: 0, 1: 1, 2: 2}[len(vowels)]
    
    # Split the message into a list of characters
    message_chars = message.split("")
    
    # Create a new list to store the encoded message
    encoded_message = []
    
    # Iterate through the characters in the message
    for char in message_chars:
        # If the character is a vowel
        if char in vowels:
            # Replace the character with the character 2 places ahead
            encoded_message.append(num_vowels[ord(char) - ord("a")])
        else:
            # Otherwise, append the character as is
            encoded_message.append(char)
        
    # Return the encoded message
    return "".join(encoded_message)