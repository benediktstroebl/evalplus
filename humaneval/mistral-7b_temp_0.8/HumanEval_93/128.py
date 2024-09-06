
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
    # 
    # Write your code here
    # 
    message=message.lower()
    result=[]
    for letter in message:
        if letter in "aeiou":
            if letter == "a":
                result.append("c")
            elif letter == "e":
                result.append("g")
            elif letter == "i":
                result.append("k")
            elif letter == "o":
                result.append("q")
            elif letter == "u":
                result.append("w")
        else:
            result.append(letter.upper())
    return "".join(result)

    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    #
