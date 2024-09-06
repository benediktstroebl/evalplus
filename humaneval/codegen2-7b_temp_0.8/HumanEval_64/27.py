
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
    y_count = s.count("y")
    count = 0
    for char in s:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
        elif char == "y":
            count += 1
            if count == y_count + 1:
                count += 1
    return
