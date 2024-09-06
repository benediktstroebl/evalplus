
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
    a = s.lower().count("a")
    e = s.lower().count("e")
    i = s.lower().count("i")
    o = s.lower().count("o")
    u = s.lower().count("u")
    y = s.lower().count("y")
    v = a+e+i+o+u
    return v+y


