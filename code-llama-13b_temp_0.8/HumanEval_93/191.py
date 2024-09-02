
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
    encoded_message = ""
    vowels = "aeiouAEIOU"
    for letter in message:
        # Is this letter a vowel?
        if letter in vowels:
            # What is the index of the vowel in the alphabet?
            # We use ord() to get the ASCII code of the letter
            # then we subtract ord('a') to normalize it to 0-indexed.
            # Now we can just add 2 to get the index of the letter
            # 2 places ahead of the original letter in the alphabet.
            vowel_index = ord(letter) - ord('a') + 2
            # Handle wraparound
            if vowel_index > 25:
                vowel_index -= 26
            # We want to use chr() to get the letter from its ASCII code.
            # But we need to add ord('a') to re-normalize it.
            vowel_index = chr(vowel_index + ord('a'))
            # Add it to the encoded message
            encoded_message += vowel_index
        else:
            # This is a consonant, so just copy it over
            encoded_message += letter
    return encoded_message
