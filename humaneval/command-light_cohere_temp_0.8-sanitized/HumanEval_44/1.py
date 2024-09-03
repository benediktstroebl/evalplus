def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    Args:
        x: int, input number
        base: int, base to convert to
    Returns:
        str: string representation of the number after base conversion
    """
    if x < 0 or base < 2:
        raise ValueError("Input values must be positive and base must be greater than 2")
    new_base = [0] * (base - 1)
    new_base[0] = 1
    new_base[1] = x
    for i in range(2, base):
        new_base[i] = new_base[i - 1] * 10
    return new_base[base - 1]