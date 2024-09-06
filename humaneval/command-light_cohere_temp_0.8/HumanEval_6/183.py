```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    nesting_level = 0
    output = []
    for char in parentheses_string:
        if char == "(":
            nesting_level += 1
        elif char == ")":
            nesting_level -= 1
        else:
            stack.push(nesting_level)
            if nesting_level == 0:
                output.append(int(char))
    return output
def test_parse_nested_parens() -> None:
    test_string = "(()()) ((())) () ((())())"
    expected_output = [2, 3, 1, 3]
    assert parse_nested_parens(test_string) == expected_output
if __name__ == "__main__":
    test_parse_nested_parens()
```
This code implements the `parse_nested_parens` function that parses and returns the deepest level of nesting of parentheses from a given string. It uses a stack to keep track of the nesting level and pushes and pops levels accordingly. The `test_parse_nested_parens` function provides test cases to verify the correctness of the `parse_nested_parens` function.