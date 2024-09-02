
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
    lst = list(message)
    lst = list(filter(str.isalpha, lst))
    vowels = ['a', 'e', 'i', 'o', 'u']

    def mapping(char):
        if char.isupper():
            char = char.lower()
        elif char.islower():
            char = char.upper()
        return char

    def next_char(char):
        return chr(ord(char) + 3)

    new_message = "".join(map(mapping, lst))
    for i in range(len(new_message)):
        if new_message[i].lower() in vowels:
            new_message = new_message[:i] + next_char(new_message[i]) + \
                new_message[i+1:]
    return new_message
