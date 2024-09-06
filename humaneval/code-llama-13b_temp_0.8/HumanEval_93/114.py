
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
    output = ''
    for letter in message:
        if letter.isalpha():
            # Check if letter is uppercase
            if letter.isupper():
                letter = letter.lower()
                if letter in 'aeiou':
                    new_letter = chr((ord(letter) - ord('a') + 2) % 26 + ord('A'))
                else:
                    new_letter = chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
            # Check if letter is lowercase
            elif letter.islower():
                if letter in 'aeiou':
                    new_letter = chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
                else:
                    new_letter = chr((ord(letter) - ord('a') + 2) % 26 + ord('a'))
            output += new_letter
        else:
            output += letter
    return output
    
