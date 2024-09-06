from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for tier in s.split():
        open_brackets = []
        close_brackets = []
        nesting = 0
        for b in tier:
            if b == '(':
                open_brackets.append(nesting)
                nesting += 1
            else:
                close_brackets.append(nesting)
                nesting -= 1
        result.append(max(open_brackets))
    return result