
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

    # return len([i for i in "aeiou" if i in s or (i in "y" and s.index(i) == len(s) - 1)])
    # return len([x for x in s if x in 'aeiou' or (x == 'y' and s.find(x) == len(s) - 1)])
    vowels = 'aeiouy'
    count = 0
    for ch in s:
        if ch in vowels or (ch == 'y' and s.index(ch) == len(s) - 1):
            count += 1
    return count
