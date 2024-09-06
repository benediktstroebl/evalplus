from typing import List
def string_xor(a: str, b: str) -> str:
    return bin(int(''.join(map(int, a+b))) ^ int(''.join(map(int, a)) ^ int(''.join(map(int, b))))).replace('0b', '')