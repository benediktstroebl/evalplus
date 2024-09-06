from typing import List
def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    curr_depth = 0

    for char in paren_string:
        if char == '(':
            curr_depth += 1
        else:
            depths.append(curr_depth)
            curr_depth = 0

    depths.append(curr_depth)

    return depths