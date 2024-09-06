def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    """
    vowels = set('aeiouy')
    count = 0
    for char in s:
        if char in vowels or (char == 'y' and s.endswith(char)):
            count += 1
    return count