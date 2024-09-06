def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel at the end of the word."""
    # Your code here!
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count