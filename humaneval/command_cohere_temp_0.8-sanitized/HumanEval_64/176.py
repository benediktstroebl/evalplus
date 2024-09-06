def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowel = "AEIOUaeiou"
    count = 0
    if s.endswith("y") and s[-.3] in vowel:
        count += 1
    for char in s:
        if char in vowel:
            count += 1
    return count