from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for separated_string in s.split():
        string = ''.join(separated_string.split())
        count = 0
        depth = 0
        nonlocal result
        i = 0
        while i < len(string):
            if string[i] == '(':
                count += 1
                depth = max(depth, count)
            elif string[i] == ')':
                count -= 1
            i += 1
        result.append(depth)
    return result