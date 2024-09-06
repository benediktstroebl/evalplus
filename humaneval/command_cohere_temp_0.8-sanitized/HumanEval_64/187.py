def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel only at the end of the word."""
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels or (char == 'y' and s[-1] == char):
            count += 1
    return count