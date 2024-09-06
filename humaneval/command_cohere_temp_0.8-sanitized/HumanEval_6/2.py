from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    result: List[int] = []
    depth: int = 0
    for char in s:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        result.append(depth)
    return result