
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
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    
    frst = -1
    scnd = -1
    for char in message:
        if char in vowels:
            scnd = scnd + 1
            if frst == -1:
                frst = scnd
        elif char != ' ':
            scnd = -1
        else:
            scnd = -1
    
    
    
    
    # declare possible replacements
    dict = {}
    dict['a'] = ['A', 'a', 'A', 'a']
    dict['e'] = ['E', 'E', 'E', 'e']
    dict['i'] = ['I', 'I', 'I', 'i']
    dict['o'] = ['O', 'O', 'O', 'o']
    dict['u'] = ['U', 'U', 'U', 'u']
    dict['y'] = ['Y', 'Y']
    # create new string
    new_msg = ''
    
    for index, char in enumerate(message):
        if char in vowels:
            # if first vowel
            if frst == -1:
                new_char = message[index + 1]
                if new_char in dict[char]:
                    new_msg = new_msg + new_char
                else:
                    new_msg = new_msg + char
            # if second vowel
            elif scnd == -1:
                new_char = message[index + 2]
                if new_char in dict[char]:
                    new_msg = new_msg + new_char
                else:
                    new_msg = new_msg + char
            # if neither vowel
            else:
                new_msg = new_msg + char
        else:
            new_msg = new_msg + char
    return new_msg

