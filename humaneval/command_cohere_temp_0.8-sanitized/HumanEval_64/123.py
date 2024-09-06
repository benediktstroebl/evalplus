def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    It considers the vowels to be 'a', 'e', 'i', 'o', 'u', and 'y' 
    only when it is at the end of the word.
    """
    num_vowels = 0
    for char in s:
        if char in 'aieou': 
            num_vowels += 1
        elif char == 'y' and s.endswith(char):
            num_vowels += 1
    return num_vowels