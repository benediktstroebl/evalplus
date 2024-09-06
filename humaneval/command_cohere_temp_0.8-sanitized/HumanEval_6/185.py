from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nest in s.split():
        if not nest:
            result.append(0)
            continue
        count = 0
        i = 0
        while i < len(nest):
            if nest[i] == '(':
                count += 1
            elif nest[i] == ')':
                count -= 1
            i += 1
        result.append(count)
    return result