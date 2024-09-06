from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.count('1') == b.count('1') != 0, "Input strings must have equal number of `1` characters for XOR."
    for i, char in enumerate(a):
        result += str(int(char) ^ int(b[i]))
    return result