from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        lev = 0
        i = 0
        while i < len(chunk):
            if chunk[i] == '(':
                lev += 1
            else:
                lev -= 1
            i += 1
        result.append(lev)
    return result