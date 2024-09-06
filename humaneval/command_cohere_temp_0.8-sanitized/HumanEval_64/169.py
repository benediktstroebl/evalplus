def vowels_count(s):
    """Returns the number of vowels in a string s,
       considering 'y' a vowel only at the end of the word.
    """
    # your code here
    total = 0
    for char in s:
        if char in 'aieou':
            total += 1
        elif char == 'y' and s[-1] == 'y':
            total += 1
    return total