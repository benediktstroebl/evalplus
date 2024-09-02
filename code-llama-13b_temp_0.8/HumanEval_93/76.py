
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
    vowels = "aeiouAEIOU"
    new_message = []
    
    for letter in message:
        if letter.isalpha():
            if letter.lower() in vowels:
                index = vowels.index(letter.lower())
                if index == 4:
                    new_message.append(vowels[0].upper() if letter.isupper() else vowels[0])
                else:
                    new_message.append(vowels[index+2].upper() if letter.isupper() else vowels[index+2])
            else:
                new_message.append(letter.swapcase())
        else:
            new_message.append(letter)
            
    return "".join(new_message)
