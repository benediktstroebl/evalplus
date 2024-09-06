def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    It considers the vowels as 'a', 'e', 'i', 'o', 'u', and also 'y' 
    as a vowel when it is at the end of the word.
    """
    tally = 0
    for c in s:
        if c in 'aieou':
            tally += 1
        elif c == 'y' and s[-1] == 'y':
            tally += 1
    return tally