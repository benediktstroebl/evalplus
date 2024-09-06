def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)