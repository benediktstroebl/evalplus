def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    import re

    pattern = re.compile(r'(A|E|I|O|U){2,}(?![^A-Z])', flags=re.I)
    matches = pattern.findall(s)
    return sum(1 for _ in matches)