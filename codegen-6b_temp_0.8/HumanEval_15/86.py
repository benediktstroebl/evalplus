

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(i) for i in range(n+1))


"""
In this project, we will use the following alphabet:

'a' through 'z', lower case
'A' through 'Z', upper case
'0' through '9'

We will use the following symbols:

'*' is a vowel (a, e, i, o, u)
'-' is a consonant
'+' is a consonant, not a vowel
"""

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
