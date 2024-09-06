def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # To count the number of vowels in a word, we use string methods
    # to find all occurrences of vowels in a word (excluding 'y' if not
    # at the end of the word) and add them to a counter, which is then
    # returned.
    import re

    vowel_regex = re.compile(r'(?i)[aeiou]{1,2}|y$')
    return sum(1 for _ in vowel_regex.finditer(s))