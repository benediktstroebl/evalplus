def vowels_count(s):
    """Returns the number of vowels in a string s, with the exception of y being a vowel only at the end of the word."""
    vowel_count = 0
    for char in s:
        if char in 'aieou' or (char == 'y' and s[-1] == 'y'):
            vowel_count += 1
    return vowel_count