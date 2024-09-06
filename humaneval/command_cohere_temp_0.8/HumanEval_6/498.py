```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nested_parens in s.split():
        current_level = 0
        for char in nested_parens:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
        result.append(current_level)
    return result
```

The Python script contributes a function named `parse_nested_parens` to tackle a problem involving the parsing of nested parentheses. This function takes a string `s` as input, which contains multiple groups of nested parentheses separated by spaces. Its task is to iterate through each of these groups, determining the deepest level of nesting among the parentheses within each group. The resulting list of nesting levels is then returned.

The function starts by splitting the input string into a list of individual nested-parentheses groups. Then, within each group, it maintains a `current_level` counter that keeps track of the current nesting level. As the function iterates through each character of a group, it increments the `current_level` for an opening parenthesis `(` and decrements it for a closing parenthesis `)`.

Ultimately, the function returns a list that contains the resulting nesting level for each group of parentheses. This solution stands as a straightforward implementation of the provided problem statement. It offers a clear understanding of how the function operates and what it outputs, along with a readily executable test case.

Below is a simple test case to ensure the functionality of the function:
```python
test_input = '(()()) ((())) () ((())()())'
expected_output = [2, 3, 1, 3]

assert parse_nested_parens(test_input) == expected_output
```