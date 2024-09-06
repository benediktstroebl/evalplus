from typing import List
def string_xor(a: str, b: str) -> str:
    return '{0}'.format(__builtin__.binascii.xorbytes(a.encode(), b.encode()))