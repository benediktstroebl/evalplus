def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    vowels are 'a', 'e', 'i', 'o', 'u' and 'y' as a vowel at the end of a word.
    """
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count