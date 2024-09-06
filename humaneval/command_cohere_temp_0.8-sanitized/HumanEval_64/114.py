def vowels_count(s):
    """Returns the number of vowels in a string s,
    including special case for 'y' as a vowel at the end of the word"""
    import re

    return sum(1 for char in s if re.search(r'[aeiou]+$', s))