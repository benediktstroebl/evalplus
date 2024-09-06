```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes in a string of parenthesis groups and returns a list of deepest level of nesting.
    Format: [()] [((()))] [()]
    """
    # Use python's re module to split the string by spaces into a list of substrings
    parent_list = [p for p in parent_string.split()]

    # Iterate through each group of parentheses, and for each level, push out the deepest level.
    max_depth = 0
    results = []
    for parent in parent_list:
        if len(parent) == 0:
            break
        elif parent[0] == '(':
            if len(results) == 0:
                results.append(1)
                max_depth = 2
            continue
        elif parent[0] == '(' and parent[-1] == ')':
            if len(results) == 0:
                results.append(max_depth + 1)
                max_depth += 2
            else:
                results[-1] = max_depth + 1
                max_depth = results[-1]
        else:
            results.append(max_depth + 1)
            max_depth += 2
    return results
```