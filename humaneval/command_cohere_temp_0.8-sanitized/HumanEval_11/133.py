from typing import List
def string_xor(a: str, b: str) -> str:
    return '{0}{1}{2}'.format(a[0] ^ b[0], a[1:].replace('0', '0' if a[0] ^ b[0] == '1' else '1'), a[0] if a[0] ^ b[0] == '0' else '1')