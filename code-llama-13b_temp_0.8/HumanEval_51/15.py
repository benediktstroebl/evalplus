

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = ['a','e','i','o','u']
    text_list = text.split()
    output_text = ''
    for word in text_list:
        for letter in word:
            if letter.lower() not in vowels:
                output_text += letter
        output_text += ' '
    return output_text.rstrip()


