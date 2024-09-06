from typing import List
def string_xor(a: str, b: str) -> str:
    return '{0}{1}'.format(*[int(x) ^ int(y) for x, y in zip(a, b) if x == '1' or y == '1'])