
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
    #print("message is", message)
    for i in range(0, len(message)):
        #print("i is ", i)
        if i == len(message) - 1:
            #print("last index i", i)
            print(message[i])
            break
        else:
            if message[i].lower() in vowels:
                #print("message[i] is", message[i])
                print(message[i+2], end="")
                i += 1
            else:
                print(message[i], end="")
        #print("end of i is", i)
