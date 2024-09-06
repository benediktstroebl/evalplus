
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
    # Dictionary to map characters to their ASCII value
    ascii_map = {
        '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53,
        '6': 54, '7': 55, '8': 56, '9': 57, 'a': 65, 'b': 66, 'c': 67,
        'd': 68, 'e': 69, 'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74,
        'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 'p': 80, 'q': 81,
        'r': 82, 's': 83, 't': 84, 'u': 85, 'v': 86, 'w': 87, 'x': 88,
        'y': 89, 'z': 90, 'A': 74, 'B': 73, 'C': 72, 'D': 71, 'E': 70,
        'F': 69, 'G': 68, 'H': 67, 'I': 66, 'J': 65, 'K': 64, 'L': 63,
        'M': 62, 'N': 61, 'O': 60, 'P': 59, 'Q': 58, 'R': 57, 'S': 56,
        'T': 55, 'U': 54, 'V': 53, 'W': 52, 'X': 51, 'Y': 50, 'Z': 49
    }

    # Create a list to store the new word
    new_word = []

    # Iterate through each character in the string
    for char in s:
       
