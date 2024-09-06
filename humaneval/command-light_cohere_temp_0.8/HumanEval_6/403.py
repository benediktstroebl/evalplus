```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [i for i, ch in enumerate(s, 2)] if ch == '(' and s.fetch[i-1] == '(' else s[i-1:]]
def test_parse_nested_parens(test_strs: List[str]) -> None:
    for test_str in test_strs:
        parsed = parse_nested_parens(test_str)
        assert parsed == [2, 3, 1, 3], f"for input: {test_str}"
if __name__ == "__main__":
    test_strs = [
        "(()()) ((())) () ((())())",
        "(((((()))))))",
        "(((((((())))))))))",
        "((())()()())",
    ]
    test_parse_nested_parens(test_strs)
```
This Python code defines a function `parse_nested_parens` that parses and returns the deepest level of nesting of parentheses in a given string. The `test_parse_nested_parens` function is used to test the `parse_nested_parens` function with a list of test strings. The `if __name__ == "__main__":` condition ensures that the test code is executed only when the script is run directly, not imported as a module.

The test strings are also provided to verify the function's behavior. The output of the code is the list of integers representing the depths of each nesting of parentheses.