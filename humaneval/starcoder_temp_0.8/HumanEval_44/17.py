

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Base case
    if x < base:
        return str(x)
    # Recursive case
    else:
        # Divide x by base and recursively compute the answer
        q, r = divmod(x, base)
        # Recursively compute the rest of the answer
        answer = change_base(q, base) + str(r)
        # Return the answer
        return answer
