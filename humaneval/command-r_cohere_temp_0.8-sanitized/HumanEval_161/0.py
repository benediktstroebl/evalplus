def solve(s):
    """
    Changes case of letters and reverses non-letter characters.
    Reverses the string if no letters are present.
    
    Args:
        s (str): Input string.
        
    Returns:
        str: Processed string.
    """
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    rev = False

    for char in s:
        if char in letters:
            result += letters[(letters.lower().index(char.lower()) + 15) % 52]
        else:
            rev = not rev
            result += char

    return result[::-1] if rev else result