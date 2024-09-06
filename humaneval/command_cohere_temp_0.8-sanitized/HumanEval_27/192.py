def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c.swapcase() if c.isupper() else c for c in string)