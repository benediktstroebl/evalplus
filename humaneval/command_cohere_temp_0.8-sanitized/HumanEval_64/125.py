def vowels_count(s):
    """
    Args:
        s (str): A word represented as a string.

    Returns:
        int: The number of vowels in the word.
           Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    # Your code here.
    # Make sure to consider the test cases.
    vowels = set('aeiou')
    ans = 0
    for char in s:
        if char in vowels:
            ans += 1
    if s.endswith('y') and s[-2:] != 'ay':
        ans += 1
    return ans