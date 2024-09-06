def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel at the end of the word."""
    # Your code here!
    vowels = 'aoeui'
    if s.endswith('y'):
        return sum(1 for char in s if char in vowels)
    return sum(1 for char in s if char in vowels)