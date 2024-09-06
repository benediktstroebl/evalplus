from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        nested = 0
        level = 0
        open_par = 0
        for j, c in enumerate(char):
            if c == '(':
                level += 1
                open_par += 1
            elif c == ')':
                level -= 1
                open_par -= 1
            else:
                pass
            nested = max(nested, level)
        result.append(nested)
    return result