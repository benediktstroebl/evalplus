
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
    vowels = ['a','e','i','o','u']
    
    vowels_list = list(vowels)
    vowels_list2 = list(vowels)
    
    vowels_list.append(vowels_list[0])
    vowels_list.append(vowels_list[1])
    
    vowels_list2.append(vowels_list2[3])
    vowels_list2.append(vowels_list2[4])
    
    vowels = ""
    vowels = vowels.join(vowels_list)
    vowels2 = ""
    vowels2 = vowels2.join(vowels_list2)
    
    message = message.lower()
    message = message.replace("a",vowels2[0])
    message = message.replace("e",vowels2[1])
    message = message.replace("i",vowels2[2])
    message = message.replace("o",vowels2[3])
    message = message.replace("u",vowels2[4])
    
    message = message.replace(vowels[0],vowels2[0])
    message = message.replace(vowels[1],vowels2[1])
    message = message.replace(vowels[2],vowels2[2])
    message = message.replace(vowels[3],vowels2[3])
    message = message.replace(vowels[4],vowels2[4])
    
    message = message.swapcase()
    
    return message
