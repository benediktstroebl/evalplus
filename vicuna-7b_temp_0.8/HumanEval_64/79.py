
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Define a list of strings to store the counts of each vowel
    counts = ['a', 'e', 'i', 'o', 'u']
    # Initialize a variable to store the count of vowels in the string
    vowel_count = 0

    # Iterate over all the characters in the string
    for c in s:
        # If the character is a vowel, increment its count
        if c in counts:
            vowel_count += 1
        else:
            # If the character is a digit or a non-vowel letter, check if
            # it is at the end of the string
            if c.isdigit() or c not in counts:
                if s.endswith(c):
                    # If the character is at the end of the string, increment
                    # the count of the vowel whose name is the same as the
                    # character
                    vowel_count += 1

    return vowel_count
