from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    carry = False
    for i in range(len(a)):
        digit = a[i] != b[i]
        result += str(digit)
        carry = carry or digit
    if carry:
        result += '1'
    return result