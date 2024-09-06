
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    def find_vowel(message):
        for letter in message:
            if letter in vowels:
                return message.index(letter)
    
    def replacement(message, vowel_index):
        if message[vowel_index] == message[vowel_index + 2]:
            return message[:vowel_index] + message[vowel_index + 1] + message[vowel_index + 3:]
        else:
            return message[:vowel_index] + message[vowel_index].lower() + message[vowel_index + 1:]
    
    vowel_index = find_vowel(message)
    
    if vowel_index == -1:
        return message
    else:
        return replacement(message, vowel_index)
