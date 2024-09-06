
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
    
    # case1: message is a single word
    if type(message) is str:
        message = message.replace(' ', '')

        new_message = ''
        for i in range(len(message) - 2):
            if message[i].isupper() and message[i+1].isupper():
                new_message += message[i+1]
                new_message += message[i]
            elif message[i].isupper():
                new_message += message[i]

        if message[-2].isupper():
            new_message += message[-1]
        else:
            new_message += message[-2]
        return new_message

    # case2: message is a list of words
    elif type(message) is list:
        new_message = ''
        for string in message:
            for i in range(len(string) - 2):
                if string[i].isupper() and string[i+1].isupper():
                    string = string[:i+1] + string[i+2].upper() + string[i+1] + string[i]
            if string[-2].isupper():
                string += string[-1]
            else:
                string += string[-2]
            new_message += string
        return new_message
