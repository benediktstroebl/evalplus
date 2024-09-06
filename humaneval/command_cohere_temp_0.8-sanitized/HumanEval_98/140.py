def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    c = 0
    for i, char in enumerate(s):
        if char.isupper() and char in 'AEIOU' and (i%2==0):
            c+=1
    return c