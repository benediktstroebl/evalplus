```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [i for i, x in enumerate(s.group.split(' '(') if x == '(')]
def test_parse_nested_parens() -> None:
    test_cases = [
        "(()()) ((())) () ((())())",
        "((()())) ((()())) ((()))",
        "((()))) () ((()()))",
        "((())()()) () ((())()())",
        "() ((())()())",
        "((())) () () ((())())",
        "() ((()) ())",
    ]
    for test_case in test_cases:
        result = parse_nested_parens(test_case)
        assert result == [2, 3, 1, 3], f"Expected {result}, got {test_case}"
```
This code defines a function `parse_nested_parens` that parses a string representing nested parentheses. It returns a object of integer, representing the deepest level of nesting of parentheses. It uses the `enumer string` as input and returns a list of integer representing the level of nesting for each group of parentheses. The `test_parse_nested_parens` function provides a series of test cases to pass to the `parse_nested_parens` function to verify its correctness.