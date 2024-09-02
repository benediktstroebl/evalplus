
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
    # This is the list of vowels in english alphabet
    vowels = 'aeiouAEIOU'
    # Create a dictionary to keep track of the count of each letter
    letter_count = {}
    # Loop through each character of the message
    for char in message:
        # If the character is a vowel, add 2 to its count
        if char in vowels:
            letter_count[char] += 2
        # If the character is not a vowel, add 1 to its count
        else:
            letter_count[char] += 1
    # Create a dictionary to store the encoded message
    encoded_message = {}
    # Loop through each letter in the message
    for char, count in letter_count.items():
        # If the count is 1, replace the character with itself
        if count == 1:
            encoded_message[char] = char
        # If the count is greater than 1, replace the character with 
        # the letter 2 places ahead of it in the alphabet
        else:
            encoded_message[char] = chr(ord(char) + 2)
    return encoded_message