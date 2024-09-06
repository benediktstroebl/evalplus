import sys
def change_base(x, base):
    """
    Change the numerical base of input number x to base,
    returning the string representation after the conversion.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        print(f"Error: Both inputs must be integers!")
        sys.exit()
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))