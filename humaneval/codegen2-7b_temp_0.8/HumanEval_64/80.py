
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
    count = 0
    for c in s:
        if c in "aeiou":
            count += 1
        if c == "y":
            if len(s) == 1:
                count += 1
            else:
                count += 1 if s[-2] in "aeiou" else 0
    return
