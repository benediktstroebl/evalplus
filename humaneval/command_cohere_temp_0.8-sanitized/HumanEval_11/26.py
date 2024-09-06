from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.replace('1', '0').replace('0', '1') == b, "Input strings must consist only of 1s and 0s."
    
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            result += '1'
        else:
            result += '0'
    return result