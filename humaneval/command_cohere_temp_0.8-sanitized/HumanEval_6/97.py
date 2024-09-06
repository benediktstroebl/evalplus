from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        chunk = chunk.replace('(', '').replace(')', '')
        depth = 0
        unbalanced = 0
        for i in range(len(chunk)):
            if chunk[i] == '(':
                depth += 1
                unbalanced += 1
            elif chunk[i] == ')':
                depth -= 1
                unbalanced -= 1
            if depth < 0:
                unbalanced += depth
                depth = 0
        result.append(unbalanced)
    return result