from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    assert a.isalpha() and b.isalpha() and a + b == '10'*len(a) + '1'*len(b), "Input validation error"
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result