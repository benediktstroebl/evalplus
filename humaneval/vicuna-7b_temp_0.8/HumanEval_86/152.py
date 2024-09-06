
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Use a dictionary to map characters to their ASCII values
    char_to_value = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102,
                    'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108,
                    'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114,
                    's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120,
                    'y': 121, 'z': 122, 'A': 65, 'B': 66, 'C': 67, 'D': 68,
                    'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75,
                    'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82,
                    'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89,
                    'Z': 90, '0': 48, '1': 51, '2': 52, '3': 53, '4': 54, '5': 55,
                    '6': 56, '7': 57, '8': 58, '9': 59, '+': 62, '-
