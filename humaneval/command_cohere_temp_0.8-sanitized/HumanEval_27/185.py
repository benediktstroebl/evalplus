def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)