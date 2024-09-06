def vowels_count(s):
    """Returns the number of vowels in a string s, counting 'y' as a vowel 
    only when it's at the end of the word.
    """
    import re

    def is_vowel(c):
        vowels = "aeiouy"
        return c in vowels or c == "y" and re.search(r'\by$', s)

    return sum(1 for _ in s if is_vowel(_))