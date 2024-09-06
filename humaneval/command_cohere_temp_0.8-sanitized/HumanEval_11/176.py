from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.count('1') == b.count('1') != 0, "Input strings must have equal counts of 1s for XOR to be defined"
    
    for i in range(min(a.count('1'), b.count('1'))):
        result += '1' if a[i] != b[i] else '0'
    return result