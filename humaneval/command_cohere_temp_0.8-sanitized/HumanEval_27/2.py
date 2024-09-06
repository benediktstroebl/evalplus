def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c.upper() for c in string)