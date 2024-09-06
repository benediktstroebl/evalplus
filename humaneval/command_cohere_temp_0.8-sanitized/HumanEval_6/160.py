from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    stack = []
    results = []
    for chunk in s.split():
        stack = [x for x in chunk if x == '(']
        stack2 = []
        while stack:
            if stack[-1] == ')':
                stack.pop()
                stack2.append(len(stack2))
            else:
                stack2.append(stack.pop())
        results.append(max(stack2))
    return results