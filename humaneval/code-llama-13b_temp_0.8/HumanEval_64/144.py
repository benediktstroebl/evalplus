
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
    vowels = "aeiouAEIOU"
    vowels_dict = {}
    for ch in s:
        if ch in vowels:
            vowels_dict.setdefault(ch, 0)
            vowels_dict[ch] += 1
    count = 0
    for k, v in vowels_dict.items():
        if k.isupper():
            count += 1
        else:
            count += v
    return count
