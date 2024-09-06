from typing import List
def string_xor(a: str, b: str) -> str:
    return '{0}{1}{2}'.format(a[0] ^ b[0], a[1:] ^ b[1:], a[-1] ^ b[-1])