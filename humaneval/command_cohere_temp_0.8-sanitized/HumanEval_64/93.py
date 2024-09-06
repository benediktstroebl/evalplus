def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel 
    only when it's at the end of the word.
    """
    if not s:
        return 0
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s[-1] == 'y':
            count += 1
    return count