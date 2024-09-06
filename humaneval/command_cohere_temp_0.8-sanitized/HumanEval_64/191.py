def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel only at the end of the word."""
    # Your code here!
    vowels = set('aeiouy')
    return sum(1 for char in s if char in vowels)