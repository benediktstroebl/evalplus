
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
    # YOUR CODE HERE
    #encryptedMessage = ''
    #for letter in message:
    #    if letter in ['a', 'e', 'i', 'o', 'u']:
    #        i = 0
    #        if letter == 'a':
    #            i = 2
    #        elif letter == 'e':
    #            i = 4
    #        elif letter == 'i':
    #            i = 5
    #        elif letter == 'o':
    #            i = 1
    #        elif letter == 'u':
    #            i = 3
    #        newLetter = chr(ord(letter) + i)
    #    else:
    #        newLetter = letter.swapcase()
    #    encryptedMessage += newLetter
    #return encryptedMessage
    
    encryptedMessage = ''
    for letter in message:
        if letter.isupper():
            if letter in ['A', 'E', 'I', 'O', 'U']:
                i = 0
                if letter == 'A':
                    i = 2
                elif letter == 'E':
                    i = 4
                elif letter == 'I':
                    i = 5
                elif letter == 'O':
                    i = 1
                elif letter == 'U':
                    i = 3
                newLetter = chr(ord(letter) + i)
            else:
                newLetter = chr(ord(letter) - 32)
        else:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                i = 0
                if letter == 'a':
                    i = 2
                elif letter == 'e':
                    i = 4
                elif letter == 'i':
                    i = 5
                elif letter == 'o':
                    i = 1
                elif letter == 'u':
                    i = 3
                newLetter = chr(ord(letter) - 32 + i)
            else:
                newLetter = letter.swapcase()
        encryptedMessage += newLetter
    return encryptedMessage
