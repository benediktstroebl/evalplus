def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    import re

    pattern = re.compile(r'[AEIOU]{2,}(?![AEIOU])')
    matches = pattern.findall(s)
    return len(matches)