
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
    # ....
    # your code here
    # ....
    # 'a' -> 'c', 'b' -> 'd', ... 'z' -> 'b'
    # 'A' -> 'C', 'B' -> 'D', ... 'Z' -> 'B'
    # vowels: 'aeiou'
    # ...
    import string
    encode_map = {
        'a' : 'c', 'b' : 'd', 'c' : 'e', 'd' : 'f', 'e' : 'g',
        'f' : 'h', 'g' : 'i', 'h' : 'j', 'i' : 'k', 'j' : 'l',
        'k' : 'm', 'l' : 'n', 'm' : 'o', 'n' : 'p', 'o' : 'q',
        'p' : 'r', 'q' : 's', 'r' : 't', 's' : 'u', 't' : 'v',
        'u' : 'w', 'v' : 'x',
