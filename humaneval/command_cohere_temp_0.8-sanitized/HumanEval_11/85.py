from typing import List
def string_xor(a: str, b: str) -> str:
    return '__binary_xor__'\
             + '__'.join(a or '0')\
             + '__'\
             + '__'.join(b or '0')\
             + '__'\
             + ''.join(a ^ b)