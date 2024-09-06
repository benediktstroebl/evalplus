from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair in s.split():
        level = 0
        i = 0
        while i < len(bracket_pair):
            if bracket_pair[i] == '(':
                level += 1
            else:
                level -= 1
            i += 1
        result.append(level)
    return result