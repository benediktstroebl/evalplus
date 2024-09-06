
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
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    vowels = list("aeiou")
    vowels_shifted = list("ijkmquvwxyz")
    vowels_dict = dict(zip(vowels, vowels_shifted))
    upper_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    upper_vowels = list("AEIOU")
    upper_vowels_shifted = list("JKMQUVWXYZ")
    upper_vowels_dict = dict(zip(upper_vowels, upper_vowels_shifted))

    message = list(message)
    for i, char in enumerate(message):
        if char in alphabet:
            message[i] = vowels_dict.get(char, char)
        elif char in upper_alphabet:
            message[i] = upper_vowels_dict.get(char, char)
        elif char == " ":
            message[i] = " "

    message = "".join(message)
    return message

