def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    
    :param s0: First string to compare.
    :param s1: Second string to compare.
    :return: Boolean result of the comparison.
    """
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6