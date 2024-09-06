
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
    result = []
    vowels = "aeiouAEIOU"
    vowels_dict = {v: vowels[(vowels.find(v) + 2) % len(vowels)] for v in vowels}
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                letter = letter.lower()
            if letter in vowels_dict:
                result.append(vowels_dict[letter].upper())
            else:
                result.append(letter)
        else:
            result.append(letter)
    return "".join(result)
