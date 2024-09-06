Here is a Python script that contains a self-contained function that solves the problem of parsing nested parentheses:
```python
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string of nested parentheses.
    Returns a specific order: the deepest level of nesting of parentheses in the string.
    Args:
        s (string): Input string to parse

    Returns: list of integers with the deepest level of nesting
    """
    stack: List[int] = []
    output: List[int] = []
    for char in s:
        if char == "(" and stack:
            stack.append(1)
        elif char == ")" and not stack:
            stack.append(len)
        elif char == ")" and stack:
            stack.pop()
            elif char == "(":
                stack.append(1)
                output.append(stack.pop())
       max()
    long(stack))
    return output

```
This script defines a function `parse_nested_parens` that takes a string as input and returns a list of integers with the deepest level of nesting. The function uses a `stack` to keep track of the level of nesting for each group of parentheses encountered.