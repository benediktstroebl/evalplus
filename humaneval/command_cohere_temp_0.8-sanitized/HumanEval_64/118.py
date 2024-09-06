def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    vowel characters are 'a', 'e', 'i', 'o', 'u', and y at the end of a word.
    """
    tally = 0
    for c in s:
        if c in 'aieou' or (c == 'y' and s.endswith(c)):
            tally += 1
    return tally