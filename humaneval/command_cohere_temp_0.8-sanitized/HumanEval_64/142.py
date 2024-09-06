def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
    if not s.endswith('y') and s not in vowels:
        return 0
    return sum(1 for char in s if char in vowels)
    # Since the set of vowels contains only 6 characters,
    # we can just iterate through the string and count
    # the number of characters that are in the set.