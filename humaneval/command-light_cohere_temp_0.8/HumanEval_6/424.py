```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parse a string of nested parentheses.

    Parameters:
    s (string): The string of parentheses to parse

    Returns:
    list: A list of the deepest level of nesting for each group of parentheses
    """
    result = []
    for e in s:
        if e == '(':
            result.append(1)
        elif e == ')':
            if len(result) == 0:
                result.append(None)
            elif len(result) == 1:
                result.append(None)
            else:
                result.append(len[result][-1])
        else:
            result.append(int(e))
    return result

# Test the function
test_string = '(()()) ((())) () ((())()())'
test_result = parse_nested_parens(test_string)
print(test_result)  # Output should be [1, 2, 3, None]
```