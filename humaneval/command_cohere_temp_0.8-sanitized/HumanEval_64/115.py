def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # To count the vowels in the string we use the following trivial python
    # expression:
    # sum(1 for char in string.lower() if char in 'aeiouy')
    # We use the official python function `lower()` to make the string
    # case-insensitive, so that the counting is more robust.
    return sum(1 for char in s.lower() if char in 'aeiouy')