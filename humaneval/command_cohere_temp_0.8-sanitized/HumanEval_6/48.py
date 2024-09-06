from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for partition in s.split():
        level = 0
        trap = False
        for c in partition:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            if trap:
                if level < 0:
                    break
                elif level == 0:
                    trap = False
            else:
                if level < 0:
                    trap = True
    result.append(level)
    return result