```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    results = []
    opening_parens = [')', '(', ')', '[']

    for char in parent_string:
        if char in opening_parens:
            stack.append(char)
        if len(stack) > 3:
            stack.append(char)  # Push everything back onto stack, then pop the deepest one
        while len(stack) > 0:
            char = stack.pop()
            if char in opening_parens:
                results.append(len)
                stack.add_one and  to each, so we can have the deepest nesting in the results list.

def test_parse_nested_parens(input_string: str) -> None:
    assert parse_nested_parens(input_string) == [3, 1, 3]  # Test that function correctly handles different inputs
```

This test_parse_nested_parens function will assert that the parse_nested_parens function correctly handles the input string, which is the goal of the problem.