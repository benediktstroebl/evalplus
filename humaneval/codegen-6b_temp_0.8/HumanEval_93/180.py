
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
    def word_dict():
        word_list = 'abcdefgijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        word_dict = {}
        for i, letter in enumerate(word_list):
            word_dict[letter] = i
        return word_dict

    def find_vowel(letter, word_dict):
        try:
            return word_dict[letter.lower()]
        except KeyError:
            return word_dict[letter]

    def swap_case(letter, find_vowel, word_dict):
        if letter.isupper():
            return word_dict[letter.lower()].upper()
        elif letter.islower():
            return word_dict[letter]

    word_dict = word_dict()
    letter_list = list(message)
    new_letter_list = []
    for letter in letter_list:
        new_letter_list.append(swap_case(letter, find_vowel, word_dict))
    return ''.join(new_letter_list)
