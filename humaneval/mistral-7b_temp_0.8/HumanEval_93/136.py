
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
    encode_map = dict(
        A="C",
        E="G",
        I="K",
        O="Q",
        U="V",
        B="D",
        C="E",
        D="F",
        G="H",
        H="J",
        J="L",
        K="M",
        L="N",
        M="O",
        N="P",
        P="R",
        Q="S",
        R="T",
        S="W",
        T="X",
        V="Z",
        W="A",
        X="B",
        Y="C",
        Z="D",
    )

    encoded = ""

    for char in message:
        if char.isalpha():
            encoded += encode_map[char.upper()]
        else:
            encoded += char

    return encoded

