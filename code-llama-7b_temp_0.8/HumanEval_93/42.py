
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
    
    # encode the message
    # 1. make lowercase
    message = message.lower()
    # 2. get the list of vowels in the alphabet
    alphabet = ['a','e','i','o','u']
    vowels = []
    for letter in alphabet:
        if letter in message:
            vowels.append(letter)
    # 3. get the list of letters to be replaced by the letters 
    #    that appear 2 places ahead of it in the alphabet
    replace_letters = []
    for letter in alphabet:
        replace_letters.append(message[message.find(letter)+2])
    # 4. encode the message
    for i in range(len(message)):
        if message[i] in vowels:
            message = message[:i] + replace_letters[vowels.index(message[i])] + message[i+1:]
        else:
            message = message[:i] + message[i].upper() + message[i+1:]

    return message
