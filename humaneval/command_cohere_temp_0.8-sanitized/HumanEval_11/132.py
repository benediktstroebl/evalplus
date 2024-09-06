from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    a = a.strip('0')
    b = b.strip('0')
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1':
            result += '0'
        elif a[i] == '1' or b[i] == '1':
            result += '1'
    return result