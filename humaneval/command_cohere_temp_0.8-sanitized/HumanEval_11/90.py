from typing import List
def string_xor(a: str, b: str) -> str:
    return "{0}{1}{2}".format(a.strip("0").strip("1"), "^", b.strip("0").strip("1"))