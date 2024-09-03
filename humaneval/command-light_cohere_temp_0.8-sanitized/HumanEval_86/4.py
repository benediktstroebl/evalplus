def anti_shuffle(s):
    """
    Returns a shuffled version of the string.
    Args:
        string: str, input string
    Returns:
        string: str, shuffled version of the input string
    """
    letters = list(s)
    for i, char in enumerate(letters):
        if char > s.index(char):
            s = s[:i] + char + s[i:]
            letters[i] = char
    return ''.join(' '.join(letters))