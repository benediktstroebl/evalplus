from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        carry = a[i] != b[i]
        result += str(carry)
    return result