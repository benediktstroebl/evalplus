def encode(message):
    """
    Encodes the message by swapping cases of all letters and replacing vowels 
    with the letter that appears two places ahead in the alphabet.
    """
    vowels = 'aeiouAEIOU'
    return ''.join(
        char.upper() if char.islower() else char.lower() 
        for char in message 
        if char in vowels 
        for i in range(2)
        ).replace('A', 'M').replace('E', 'H').replace('I', 'O')