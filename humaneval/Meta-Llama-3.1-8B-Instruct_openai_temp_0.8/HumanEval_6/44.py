Here's a Python script that solves the problem:

```markdown
### Solution for parsing nested parentheses

```python
from typing import List

def max_nested_level(s: str) -> int:
    """ Calculate the maximum level of nested parentheses in a group.
    
    :param s: The input string to parse.
    :return: The maximum level of nested parentheses.
    """
    level = 0
    max_level = 0
    for char in s:
        if char == '(':
            level += 1
            max_level = max(max_level, level)
        elif char == ')':
            level -= 1
    return max_level


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    
    :param paren_string: The input string to parse.
    :return: A list of maximum levels of nesting for each group.
    """
    groups = paren_string.split()
    result = []
    for group in groups:
        result.append(max_nested_level(group))
    return result


# Example usage:
if __name__ == "__main__":
    test_string = '(()()) ((())) () ((())()())'
    print(parse_nested_parens(test_string))  # Output: [2, 3, 1, 3]
```

This script defines two functions: `max_nested_level` calculates the maximum level of nested parentheses in a given group, and `parse_nested_parens` splits the input string into groups and applies `max_nested_level` to each group. The `if __name__ == "__main__":` block demonstrates how to use `parse_nested_parens` with an example input string.