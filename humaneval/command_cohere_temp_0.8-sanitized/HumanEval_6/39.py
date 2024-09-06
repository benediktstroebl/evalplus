from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses."""
    def max_depth(stack, current_depth, s):
        if not s:
            return current_depth
        elif s[0] == '(':
            stack.append(s)
            return max_depth(stack, current_depth + 1, s[1:])
        elif s[0] == ')':
            open_braces = 0
            while stack and stack[-1] != s:
                open_braces += 1
                stack.pop()
            return max(open_braces, current_depth)
        else:  # spaces are separators
            return max_depth(stack, current_depth, s[1:])

    return [max_depth( [], 0, group.strip() ) for group in s.split()]