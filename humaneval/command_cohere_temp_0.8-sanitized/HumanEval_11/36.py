from typing import List
def string_xor(a: str, b: str) -> str:
    result = ''
    mask = '' 
    for i in range(min(len(a), len(b))):
        if a[i] == '1':
            if b[i] == '0':
                result += '1'
            elif b[i] == '1':
                result += '0'
        elif a[i] == '0':
            if b[i] == '1':
                result += '1'
            elif b[i] == '0':
                result += '0'
        # Add extra 0s to a and b so we can use them as masks
        a += '0' * (len(b) - len(a))
        b += '0' * (len(a) - len(b)) 
        mask += '1' * (len(a) - len(b)) 
    return result + mask