from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        result += str((int(a[i]) ^ int(b[i])) % 2)
    return result