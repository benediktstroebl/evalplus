def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    import re

    pattern = re.compile(r'[AEIOU]{2,}[12579]')
    return sum(1 for _ in pattern.finditer(s))