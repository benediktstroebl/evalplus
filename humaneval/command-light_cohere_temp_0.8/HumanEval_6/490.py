```python
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with nested parentheses and returns a list of the deepest level of parentheses.
    :param s: str containing a string of nested parentheses
    :return: list of the deepest level of parentheses
    """
    stack = []
    new_level = 0
    result = []

    for char in s:
        if char == "(":
            stack.append(new_level)
            new_level += 1
        elif char == ")":
            if len(stack) == 0:
                return []
            stack.pop()
            level = stack.pop()
       
            level = new_level
        else:
            continue

    return result

# Example usage
test_str = "(()()) ((())) () ((()))"
test_result = parse_nested_parens(test_str)
print(test_result)
```

This script defines a function called **parse_nested_parens** that takes a string s as input and returns a list of the deepest level of parentheses in the string. The function uses a stack to keep track of the open parentheses and the current level. The function iterates over the levels of nesting and returns the result as the deepest level of parentheses.

The script also includes an example usage of the function, passing the string with the markdown code block as an argument and printing the resulting list of parentheses.