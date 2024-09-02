
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    # Use a dictionary to map each letter to its index
    # in the alphabet
    letter_index = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6,
        'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
        'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
        't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
        'z': 25, 'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30,
        'F': 31, 'G': 32, 'H': 33, 'I': 34, 'J': 35, 'K': 36,
        'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42,
        'R': 43, 'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48,
        'X': 49, 'Y': 50, 'Z': 51, 'J': 52, 'K': 53, 'L': 54,
        'M': 55, 'N': 56, 'O': 57, 'P': 58, 'Q': 59, 'R': 60,
        'S': 61, 'T': 62, 'U': 63, 'V': 64, 'W': 65, 'X': 66,
        'Y': 
