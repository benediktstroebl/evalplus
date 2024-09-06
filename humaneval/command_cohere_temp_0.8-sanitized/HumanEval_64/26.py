def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    It defines 'y' as a vowel only when it is at the end of the word.
    """
    import re

    def is_vowel(c):
        vowels = "aeiouy"
        return c in vowels or c == "y" and re.search(r'\by$', s)

    return sum(1 for char in s if is_vowel(char))