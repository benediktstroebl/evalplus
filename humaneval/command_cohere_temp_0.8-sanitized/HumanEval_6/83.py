from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
For each of the group, output the deepest level of nesting of parentheses."""
    def max_depth(stack, current_depth, i):
        if i == len(s):
            return current_depth
        else:
            char = s[i]
            if char == '(':
                stack.append(i)
                max_depth(stack, current_depth + 1, i + 1)
                stack.pop()
            elif char == ')':
                if stack and stack[-1] <= i:
                    current_depth = max(current_depth, max_depth(stack, current_depth + 1, stack.pop()))
                else:
                    current_depth += 1
            return current_depth
    return [max_depth(i, 0, 0) for i in range(len(s.split()))]