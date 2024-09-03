def digitSum(s):
    """Returns the sum of ASCII codes of uppercase digits in the input string.

    Args:
        s (str): Input string.

    Returns:
        int: Sum of ASCII codes of uppercase characters.
    """
    return sum(ord(c) for c in s if c.isupper())