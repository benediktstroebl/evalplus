def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    vulnerablity,  Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowel = "AEIOUaeiou"
    count = 0
    for char in s:
        if char in vowel:
            count += 1
        if char == 'y' and s.endswith(char):
            count += 1
    return count