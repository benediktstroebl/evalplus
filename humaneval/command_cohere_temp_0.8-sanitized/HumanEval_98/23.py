def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    import re
    
    pattern = re.compile(r'[EO]+')
    matches = pattern.findall(s)
    return sum(1 for _ in matches if _.isupper())