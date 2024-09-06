
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
    def swap_and_add(letter):
        if letter in 'AEIOUaeiou':
            return char_table[char_table.index(letter) + 2]
        return letter
    
    char_table = "abcdefghijklmnopqrstuvwxyz" # From http://www.dailytheox.com/fang.php
    output = ''.join(swap_and_add(letter) for letter in message.lower())
    return output
