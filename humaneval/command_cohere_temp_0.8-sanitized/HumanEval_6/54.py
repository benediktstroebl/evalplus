from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        nesting = 0
        level = 0
        start = 0
        for c in char:
            if c == '(':
                nesting += 1
                if nesting == 1:
                    start = i+1
                else:
                    level = max(level, nesting)
            elif c == ')':
                nesting -= 1
        result.append(level)
    return result