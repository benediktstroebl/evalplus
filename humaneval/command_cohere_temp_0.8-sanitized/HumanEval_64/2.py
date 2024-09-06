def vowels_count(s):
    """
    This function counts the number of vowels in a string, including special case 'y' as a vowel at the end of a word.
    """
    vowel = "aeiouy"
    count = 0
    for char in s:
        if char in vowel:
            count += 1
    # check if last character is 'y'
    if s[-1] == 'y' and s[-2] != 'e':
        count += 1
    return count