def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # To count the number of vowels in a word, we can use a list comprehension to identify all vowels in the word.
    # If the letter is a vowel or a Y at the end of the word, it is included in the list; otherwise, it is not included.
    # The length of this list is then the number of vowels in the word.
    return len([c for c in s if c in 'aeiouy' or (c == 'y' and s[-1] == 'y')])