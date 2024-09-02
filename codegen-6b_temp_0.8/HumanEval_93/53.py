
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
    dictionary = {'a':'y',
                  'b':'v',
                  'c':'z',
                  'd':'w',
                  'e':'x',
                  'f':'u',
                  'g':'t',
                  'h':'s',
                  'i':'r',
                  'j':'q',
                  'k':'p',
                  'l':'o',
                  'm':'n',
                  'n':'m',
                  'o':'l',
                  'p':'k',
                  'q':'j',
                  'r':'i',
                  's':'h',
                  't':'g',
                  'u':'f',
                  'v':'e',
                  'w':'d',
                  'x':'c',
                  'y':'b',
                  'z':'a'}

    def switch_case(char):
        """
        Switches a char to it's upper or lower version
        """
        if char.isalpha():
            return char.swapcase()
        else:
            return char

    def find_vowels(word):
        """
        Searches for vowels in a given word, returning a list of them.
        """
        vowels = []
        for i, char in enumerate(word):
            if char in 'aeiou':
                vowels.append(char)
        return vowels

    def replace_vowels(word, v):
        """
        Replaces vowels with those that appear 2 places ahead of them. 
        """
        word = list(word)
        for i, char in enumerate(word):
            if char == v:
                word[i] = dictionary[v]
        return ''.join(word)

    def replace_letters(word):
        """
        Iterates over the given word, replacing all vowels with the
        letters that appear 2 places ahead of them.
        """
        for i, char in enumerate(word):
            if char in 'aeiou':
                word[i] = dictionary[char]
        return word

    return ''.join(list(map