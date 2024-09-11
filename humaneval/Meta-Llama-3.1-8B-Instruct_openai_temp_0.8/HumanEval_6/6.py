```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses as input, where each group of parentheses is separated by a space.
    It returns a list of integers, where each integer represents the maximum depth of nesting for the corresponding group of parentheses.

    Args:
    paren_string (str): A string of nested parentheses.

    Returns:
    List[int]: A list of integers representing the maximum depth of nesting for each group of parentheses.
    """
    result = []
    temp_groups = paren_string.split()

    for group in temp_groups:
        max_depth = 0
        depth = 0

        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                depth -= 1

        result.append(max_depth)

    return result


# Example usage:
if __name__ == "__main__":
    input_string = '(()()) ((())) () ((())()())'
    print(parse_nested_parens(input_string))
```

When you run this script, it will print: `[2, 3, 1, 3]`