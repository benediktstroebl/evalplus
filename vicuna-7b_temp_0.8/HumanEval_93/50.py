
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
    def fix_vowels(word):
        """
        Replace vowels with its 2nd letter in the english alphabet.
        """
        word = word.lower()
        for i in range(len(word)):
            if word[i] in "aeiou":
                if word[i] in 'aeiou':
                    word = word.replace(word[i], word[i+1])
                else:
                    word = word.replace(word[i], ' ')
        return word

    message = fix_vowels(message)

    def swap_case(word):
        """
        Swap case of all letters in the word.
        """
        word = word.upper()
        for i in range(len(word)):
            if word[i] == 'a':
                word = word.replace(word[i], 'A')
            elif word[i] == 'b':
                word = word.replace(word[i], 'B')
            elif word[i] == 'c':
                word = word.replace(word[i], 'C')
            elif word[i] == 'd':
                word = word.replace(word[i], 'D')
            elif word[i] == 'e':
                word = word.replace(word[i], 'E')
            elif word[i] == 'f':
                word = word.replace(word[i], 'F')
            elif word[i] == 'g':
                word = word.replace(word[i], 'G')
            elif word[i] == 'h':
                word = word.replace(word[i], 'H')
            elif word[i] == 'i':
                word = word.replace(word[i], 'I')
            elif word[i] == 'j':
                word = word.replace(word[i], 'J')
            elif word[i] == 'k':
                word = word.replace(word[i], 'K')
            elif word[i] == 'l':
                word = word.replace(word[i], 'L')
            elif word[i] == 'm':
                word = word.replace(
