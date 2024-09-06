def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    """.strip()
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
    return sum(1 for char in s if char in vowels and (char == 'y' or s.endswith(char)))