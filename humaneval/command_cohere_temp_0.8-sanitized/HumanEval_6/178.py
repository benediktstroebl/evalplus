from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_seq in s.split():
        lev = 0
        for c in bracket_seq:
            if c == '(':
                lev += 1
            else:
                lev -= 1
            result.append(lev)
    return result