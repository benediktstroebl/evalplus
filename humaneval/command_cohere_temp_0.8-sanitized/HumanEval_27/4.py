def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.islower() else char.upper() for char in string)