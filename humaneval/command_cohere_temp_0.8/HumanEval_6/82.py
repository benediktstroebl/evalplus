Here's a Python script with a self-contained function that solves the problem using a recursive approach and passes the provided tests:
```python
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
```

The provided example and tests are included and can be run by commenting the corresponding lines:
```python
# Example test
paren_string = '(()()) ((())) () ((())()())'
print(parse_nested_parens(paren_string))

# Test #1
paren_string = '(()()) ((()))'
print(parse_nested_parens(paren_string))

# Test #2
paren_string = '() () () () () () () () ()'
print(parse_nested_parens(paren_string))

# Test #3
paren_string = '()'
print(parse_nested_parens(paren_string))
```

This script uses a recursive approach, splitting the input string on spaces, and then recursively checking the nesting level for each substring. The function takes a string as input and returns a list of the deepest nesting level for each substring.