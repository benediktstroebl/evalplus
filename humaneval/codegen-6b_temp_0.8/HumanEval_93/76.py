
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
    letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    letter_chars = "".join(letters)
    
    vowels = "AEIOUaeiou"
    vowel_chars = "".join(vowels)
    
    message = message.upper()
    
    i_letters = list(message)
    
    for i in range(len(i_letters)):
        if i_letters[i] in letter_chars:
            i_letters[i] = letters[letter_chars.find(i_letters[i]) + 2]
        
        if i_letters[i] in vowel_chars:
            i_letters[i] = letters[vowel_chars.find(i_letters[i]) + 2]
    
    return "".join(i_letters)

