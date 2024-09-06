def vowels_count(s):
    """Returns the number of vowels in a string, counting 'y' as a vowel only at the end."""
    vowel_count = 0
    for char in s:
        if char in 'aieou':
            vowel_count += 1
        elif char == 'y' and s.endswith('y'):
            vowel_count += 1
    return vowel_count