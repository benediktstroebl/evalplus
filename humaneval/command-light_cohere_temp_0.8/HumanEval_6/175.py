Here is a self-contained Python script that solves the problem:
```python
def parse_nested_parens(s: str) -> List[int]:
    """
    This function returns the deepest level of nesting of parentheses in the given string.
    Args:
        s (string): str to be checked for nested parentheses

    Returns:
    List of indices of each level of nesting found
    """
    stack: List[int] = []
    result: List[int] = []

    for i, char in enumerate(s):
        if char == ")":
            stack.append(i)
        if len(stack) == 0:
            result.append(i)
            stack.append(None)
        elif len(stack) == 1:
            result.append(len(stack) - 1)
            stack.pop()
        else:
                result.append(len(stack) - 2)
                stack.pop()

    return result

    ```
    test_deep_nest_pass():
    assert parse_nested_parens('(()()) ((())) () ((()))()')[2, 3, 1, 3] == [2, 3, 1, 3]
    test_nested_value_pass():
    assert parse_nested_parens('((())) () ((()))()')[1, 2, 3] == [1, 2, 3]
    test_single_nest_pass():
    assert parse_nested_parens('()()()()()()()())[1, 2, 3] == [1, 2, 3]
    test_double_nest_pass():
    assert parse_nested_parens('(()()) (((()()()()()()()()))))[1, 2, 3] == [1, 2, 3]
    test_long_value_pass():
    assert parse_nested_parens('(())( (((())) ))()())[1, 2, 3] == [1, 2, 3]') == [1, 2, 3]
```
The above code defines the `parse_nested_parens` function that takes a string of characters as input and returns a list of indices of each level of nesting found. 
The `test_deep_nest_pass`, `test_nested_value_pass`, `test_single_nest_pass`, and `test_double_nest_pass` functions are used to test the `parse_nested_parens` function with different inputs. 
Please note that this script is self-contained and does not require any additional modules or functions.