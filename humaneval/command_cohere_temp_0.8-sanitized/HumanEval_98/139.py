def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    counter = 0
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in 'AEIOU':
            counter += 1
    return counter