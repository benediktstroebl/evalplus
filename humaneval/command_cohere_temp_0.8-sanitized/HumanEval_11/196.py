from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    a, b = map(lambda x: int(x) ^ int(y) for x, y in zip(a, b))
    for val in zip(a, b):
        result += str(val)
    return result