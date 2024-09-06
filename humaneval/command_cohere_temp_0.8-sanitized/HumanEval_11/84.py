from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.count('1') == b.count('1') == len(a) // 2, "Input strings must have the same number of 1s for the same length"
    
    for i in range(len(a)):
        if a[i] == '1':
            result += '1' if b[i] == '0' else '0'
        else:
            result += '0' if b[i] == '1' else '1'
            
    return result