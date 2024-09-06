

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.upper()
    return ''.join([chr(ord(c) ^ 0x40) for c in string])

def pair_words(string: str) -> str:
    """ Pairs words in a string, wrapping if necessary.
    >>> pair_words('Hello, World!')
    'Hello World,!'
    """
    words = string.split(', ')
    word_pairs = []
    for word1, word2 in zip(words[::2], words[1::2]):
        word_pairs.append(f'{word1}, {word2}')
    return ', '.join(word_pairs)

def from_markdown(string: str) -> str:
    """ Converts a string from Markdown to plain text.
    >>> from_markdown('*This is a heading\n*in markdown*')
    'This is a heading\nin markdown'
    """
    string = string.replace('*', '').strip()
    return string