from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.replace('1', '0').replace('0', '1') == b, "Input validation error"
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result