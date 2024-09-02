
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
    swapped_message = ''
    
    for char in message:
        if char.isupper():
            swapped_message += char.lower()
        elif char.islower():
            swapped_message += char.upper()
        else:
            swapped_message += char
    
    vowel_count = 0
    new_vowel_count = 0
    
    for i in swapped_message:
        if i in vowels:
            vowel_count += 1
    
    for i in swapped_message:
        if i in vowels:
            new_vowel_count += 2
            
    if vowel_count!= 0:
        for i in range(vowel_count):
            swapped_message = swapped_message.replace(vowels[i], vowels[new_vowel_count])
            new_vowel_count += 1
    
    return swapped_message
