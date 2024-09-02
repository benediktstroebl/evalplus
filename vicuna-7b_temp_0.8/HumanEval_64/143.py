
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
    # Check if the word is empty
    if not s:
        return 0

    # Check if the word contains only vowels
    if 'aeiou' in s:
        return len(s)

    # Check if the word ends with 'y'
    if s[-1] == 'y':
        return len(s)

    # Otherwise, check if the word ends with 'y' and ignore it
    if s[-1] == 'y' and s[:-1].lower() not in 'aeiou':
        return len(s)

    # Check if the word ends with 'e' or 'i' followed by 'y'
    if s[-1] == 'e' or s[-1] == 'i' and s[-2] == 'y':
        return len(s)

    # Check if the word ends with 'i' or 'u' followed by 'y'
    if s[-1] == 'i' or s[-1] == 'u' and s[-2] == 'y':
        return len(s)

    # Check if the word ends with 'o' or 'u' followed by 'y'
    if s[-1] == 'o' or s[-1] == 'u' and s[-2] == 'y':
        return len(s)

    # Otherwise, check if the word ends with 'a', 'e', 'i', 'o' or 'u' followed by 'y'
    for c in s[-2:-1]:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            if c.lower() == 'y':
                return len(s)

    # Check if the word starts with 'a', 'e', 'i', 'o' or 'u' followed by 'y'
    if s[0] in 'aeiou' and s[0].lower() == 'y':
        return len(s)

    # Check if the word starts with 'aeiou' followed by 'y'
    if s[0] in 'aeiou' and s[0].lower() == 'y':
        return len(s
