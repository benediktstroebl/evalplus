from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_str in s.split():
        count = 0
        nested = 0
        level = 0
        for char in bracket_str:
            if char == '(':
                count += 1
                nested += 1
            else:
                count -= 1
                if not count:
                    level += nested
                    nested = 0
        result.append(level)
    return result