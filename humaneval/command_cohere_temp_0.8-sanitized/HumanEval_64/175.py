def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowel = "aeiou"
    count = 0
    for char in s:
        if char in vowel or (char == 'y' and s[-1] == char):
            count += 1
    return count