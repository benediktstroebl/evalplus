
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
    for i in message:
        if i in "AEIOU":
            index = "AEIOU".index(i)
            print(index)
            print(index + 2)
            print("AEIOU")
            print(list("AEIOU"))
            print(list("AEIOU")[index + 2])
            print("hey")
            new = list(message)
            new[index] = list("AEIOU")[index + 2]
            print(new)

