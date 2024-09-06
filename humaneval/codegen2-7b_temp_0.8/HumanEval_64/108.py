
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
    a = b = e = i = o = u = 0
    for char in s:
        if char in 'aeiou':
            a += 1
        if char in 'AEIOU':
            e += 1
        if char in 'y':
            i += 1
        if char in 'Y':
            o += 1
        if char in 'U':
            u += 1
    return a + e + i + o + u
    
    
