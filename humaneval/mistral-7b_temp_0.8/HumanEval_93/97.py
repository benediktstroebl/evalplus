
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
    # your code here
    def is_vowel(letter):
        """
        Checks if a letter is a vowel
        """
        return letter in "aeiou"

    def get_next_vowel(letter):
        """
        Gets the letter that appears 2 places ahead of the letter in the
        english alphabet
        """
        if not is_vowel(letter):
            return letter
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        vowel_index = alphabet.index(letter)
        return alphabet[vowel_index + 2]

    def to_upper(letter):
        """
        Converts a letter to uppercase
        """
        if letter == letter.lower():
            return letter.upper()
        return letter

    def to_lower(letter):
        """
        Converts a letter to lowercase
        """
        if letter == letter.upper():
            return letter.lower()
        return letter

    def swap_case(letter):
        """
