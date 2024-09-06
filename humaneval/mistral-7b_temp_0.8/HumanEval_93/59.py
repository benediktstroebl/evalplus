
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
    # BEGIN YOUR SOLUTION
    new_str = ''
    letter_list = list(message)
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(letter_list)):
        if letter_list[i].lower() in vowel_list:
            letter_list[i] = chr(ord(letter_list[i].lower()) + 2)
        elif letter_list[i].isupper():
            letter_list[i] = letter_list[i].lower()
        else:
            letter_list[i] = letter_list[i].upper()
    for i in range(len(letter_list)):
        new_str += letter_list[i]
    return new_str
    # END YOUR SOLUTION

