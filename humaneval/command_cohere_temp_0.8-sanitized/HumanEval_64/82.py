def vowels_count(s):
    """
    Args:
        s (str): A word

    Returns:
        int: Number of vowels in the word
    """
    vowels = set('aeiouy')
    y_count = s.endswith('y')
    if y_count:
        vowels.remove('y')
        vowels.add('i')
    return sum(1 for char in s if char in vowels)