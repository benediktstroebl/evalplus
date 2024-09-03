def change_base(x: int, base: int):
    """Convert numbers to different bases.
    Args:
        x (int): number to convert
        base (int): base to convert x to, base < 10
    Returns:
        str: x converted to the specified base
    """
    x = bin(x)[2:]  # Get the binary representation of x
    return ''.join([change_base_helper(int(d)) for d in x[::-1]])
def change_base_helper(x: int):
    return str(x % base) if x < base else chr(x % base + 48)