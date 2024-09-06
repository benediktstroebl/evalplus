```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string with nested parentheses as input and returns the deepest level of nesting for each group.
    :param s: Input string with nested parentheses
    :return: List of the deepest level of nesting for each group
    """
    result = []
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                result.append(0)
            stack.append(c)
    else:
                current_level = len(stack)-1
                while len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    result.append(current_level)
                    stack.append(c)
                current_level += 1
    return result

# Example test cases
test_parse_nested_paren = [parse_nested_parens('(()()) ((())) () ((()))()')]
test_parse_nested_paren. [(1: 1)
test_parse_nested_paren. [(2: 3)
test_parse_nested_paren. [(3: 3)
test_parse_nested_paren. [0]
test_parse_nested_paren. [1]
test_parse_nested_paren. [2, 3]
test_parse_nested_paren. []3: 2
```