
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
    
    # Take the message and reverse it
    # Take each character and turn it into a number
    # Find out where the number is in the alphabet
    # Turn the number + 2 into a letter
    # Add the letter to a new string
    # Reverse the new string and return
    
    # So how do you find where the letter is?
    # ord(character) - ord('a')
    
    encoded_message = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for character in message:
        vowel_check = character.lower()
        if vowel_check in 'aeiou':
            index = alphabet.index(vowel_check)
            new_letter = alphabet[index + 2]
            encoded_message += new_letter.upper()
        else:
            encoded_message += character.swapcase()
    return encoded_message[::-1]
