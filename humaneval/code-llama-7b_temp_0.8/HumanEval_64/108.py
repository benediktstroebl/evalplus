
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
    # 1st-way
    # return sum([1 for c in s if c in "aeiou" and (c.lower() != c or c == s[-1])])

    # 2nd-way
    # return sum([1 for c in s if c.lower() in "aeiou" and (c.lower() != c or c == s[-1])])

    # 3rd-way
    # return sum([1 for c in s if c.lower() in "aeiou" and (c == s[-1] or c == s[-1].lower())])

    # 4th-way
    # return sum([1 for c in s if c.lower() in "aeiou" and (c in ("a", "e", "i", "o", "u", "y") or c == s[-1])])

    # 5th-way
    # return len([c for c in s if c.lower() in "aeiou" and (c == s[-1] or c == s[-1].lower())])

    # 6th-way
    # return len([c for c in s if c in ("a", "e", "i", "o", "u") or c in ("y", "Y") or c == s[-1]])

    # 7th-way
    # return sum(c in ("a", "e", "i", "o", "u") or c in ("y", "Y") or c == s[-1] for c in s)

    # 8th-way
    # return sum(c in "aeiouyY" or c == s[-1] for c in s)

    # 9th-way
    # return sum(map(lambda c: c in "aeiouy" or c == s[-1], s))

    # 10th-way
    # return sum(1 for c in s if c in "aeiouy" or c == s[-1])

    # 11th-way
    # return sum(1 for c in s if c in "aeiouy" or c == s[-1])
    # return sum(1 for c in
