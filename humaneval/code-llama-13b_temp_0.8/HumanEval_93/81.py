
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
    shifted_message = ""
    vowels = "aeiouAEIOU"
    
    for letter in message:
        # swap case
        if letter.isalpha():
            if letter.isupper():
                letter = letter.lower()
            else:
                letter = letter.upper()
            
        # replace vowels
        if letter in vowels:
            vowel_index = vowels.find(letter)
            if vowel_index + 2 < 11:
                letter = vowels[vowel_index + 2]
            else:
                letter = vowels[vowel_index + 2 - 11]
        shifted_message += letter
        
    return shifted_message
