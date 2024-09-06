
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
    def swap_case(string):
        return string.swapcase()
    def replace_vowels(string):
        # Return string with every vowel replaced with 
        # the letter 2 places ahead in the alphabet
        vowels = 'aeiouAEIOU'
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        new_string = ""
        for letter in string:
            if letter in vowels:
                new_string += alphabet[(alphabet.index(letter)+2)%52]
            else:
                new_string += letter
        return new_string
    def run(message):
        return swap_case(replace_vowels(message))
    return run(message)
