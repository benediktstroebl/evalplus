def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if len(char) == 1 else char for char in string)