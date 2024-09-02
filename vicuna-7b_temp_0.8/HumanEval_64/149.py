
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
    # Write code here to get the count of vowels
    # You can use the string slicing operator ':[' to access the characters
    # in the string. The slice ':[' indices, str(s)[0:1] will give the
    # first character, str(s)[1:2] will give the second character, and so
    # on.
    # You can use the 'in' keyword to check if a character is a vowel or not.
    # For example, 'a in "aeiou"'.
    return sum(1 for c in s if c in "aeiou")
