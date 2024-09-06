def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    It defines 'y' as a vowel only when it is at the end of the word.
    """
    import re

    if not s:
        return 0

    # Using regex to find counts of all vowels in the string, including 'y' at the end
    yPattern = re.compile(r'[aeiou]+y$')
    vowel_count = sum(1 for _ in yPattern.finditer(s))

    return vowel_count