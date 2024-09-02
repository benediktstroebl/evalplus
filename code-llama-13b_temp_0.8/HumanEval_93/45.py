
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
    vowels = "aeiou"
    swapcase_message = message.swapcase()
    output_string = ""
    for letter in swapcase_message:
        if letter in vowels:
            vowel_index = vowels.find(letter) + 2
            if vowel_index > 6:
                vowel_index -= 6
            output_string += vowels[vowel_index]
        else:
            output_string += letter
    return output_string

