def vowels_count(s):
    """Returns the number of vowels in a string s,
    including special case 'y' as a vowel at the end of the word."""
    num_vowels = 0
    vowels = ["a", "e", "i", "o", "u", "y"]
    for char in s:
        if char in vowels:
            num_vowels += 1
    return num_vowels