
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
    result = ""
    vowels = "aeiou"
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                result += letter.lower()
            else:
                result += letter.upper()
        else:
            result += letter
    for i in range(len(result)):
        if result[i].lower() in vowels:
            current_vowel = vowels.index(result[i].lower())
            next_vowel = (current_vowel + 2) % 5
            if result[i].isupper():
                result = result[0:i] + vowels[next_vowel].upper() + result[i+1:]
            else:
                result = result[0:i] + vowels[next_vowel] + result[i+1:]
    return result
