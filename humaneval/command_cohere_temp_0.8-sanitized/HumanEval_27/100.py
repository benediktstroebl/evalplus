def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.isalpha() else char for char in string)