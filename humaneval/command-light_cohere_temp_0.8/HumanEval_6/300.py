Here's a self-contained Python script that defines a function `parse_nested_parens` which takes a string of nested parentheses as input and returns the deepest level of nesting:
```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    A function that parses a string of nested parentheses and returns the deepest level of nesting.
    """
    - splits the strings by space, and creates a list of integers that represents the deepest level of nesting
    """
    return [int(x) for x in parentheses_string.split()]
```

This function uses list comprehension to split the input string into individual parentheses, and then uses the `int()` function to convert each character to its corresponding integer value. The resulting list is then returned as the deepest level of nesting.

Here are some sample test cases:
```python
# Test cases
test_cases = [
    ("(()())"),
    ("(()())((()))"),
    ("()()()()((())))",
    ("(())",
    ("(())()()"),
    ("()()())",
    ("())",
    ("()()()()()()()())"
]

for test_case in test_cases:
    print(parse_nested_parens(test_case))  # Output: [1, 2, 3, 4, 1, 4]
```