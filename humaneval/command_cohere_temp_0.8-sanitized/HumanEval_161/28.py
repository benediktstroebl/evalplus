def solve(s):
    """
    Solve the given problem.

    Parameters:
        s (str): The input string.

    Returns:
        str: The string after the transformation.
    """
    # Your code here.
    no_letters = all(char.isdigit() or char in '#@' for char in s)
    transformed = s.swapcase() if any(char.isalpha() for char in s) else s[::-1]
    return transformed if no_letters else transformed.swapcase()