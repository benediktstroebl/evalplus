```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    # Breaking apart the string into a list of substrings
    substrings = parenthes.split()

    array of lists(substrings)
    return [match.count(b) for b in array]
def test_parse_nested_parens():
    # Test cases
    test_cases = [
        "(()()) ((())) () ((())())",
        "((((()()))))",
        "((()()()()))",
        "(())()())",
        "()()()()()",
        "(()))))"
    ]
    for test_case in test_cases:
        nested_parents = parse_nested_parens(test_case)
        expected = [2, 3, 1, 3]
        assert nested_parents == expected, f"Expected {expected}, but got {nested_parents}"
```
The code defines a function parse_nested_parens that takes a string of nested parentheses and returns a list of the counts of each level of nesting. It uses the string. The function then splits the string into a list of substrings, and then uses a list comprehension to extract the counts of each level of nesting for each substring. The test_parse_nested_parens function creates a list of test cases, and then iterates over each test case, calling the parse_nested_parens function with the test case as an argument. It uses the test assertions to check that the actual count of parentheses matches the expected count for each test case.