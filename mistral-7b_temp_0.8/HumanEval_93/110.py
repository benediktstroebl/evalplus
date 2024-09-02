
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
    # Makes a dictionary that maps a vowel to a vowel 2 places 
    # ahead.
    vowel_dict = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'z'}

    # Creates a list of letters in the message. 
    message_list = list(message)

    # Iterates through the letters in the message list. 
    for i in range(len(message_list)):
        # This if statement changes the letter to uppercase if it's a vowel.
        if message_list[i].lower() in vowel_dict:
            message_list[i] = vowel_dict[message_list[i].lower()]
        # If the letter is a vowel, it changes the case.
        elif message_list[i].lower() in 'aeiou':
            message_list[i] = message_list[i].upper()
        # If the letter is not a vowel, it does not change case.
        else:
            message_
