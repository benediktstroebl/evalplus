
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
    encoded_message = []
    vowels = ('a', 'e', 'i', 'o', 'u')
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                encoded_letter = letter.upper()
            else:
                encoded_letter = letter.lower()
            
            if encoded_letter in vowels:
                vowel_index = vowels.index(encoded_letter) + 2
                if vowel_index > 5:
                    vowel_index -= 5
                encoded_letter = vowels[vowel_index]
        else:
            encoded_letter = letter
        encoded_message.append(encoded_letter)
    return ''.join(encoded_message)
