Here's the solution to the problem you provided:

```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    results = []
    for match in parentheses_string.match(r'\((.*?)\))'):
        if match:
            group = match.group[1]
            if group:
                stack.push(group)
                results.push(1)
                stack = stack[::-1]
    return results

# Test cases
tests = [
    ("(()()) ((())) () ((())()())"),
    "((()))()()()()()()()()()()()()",
    "(((())))()",
    "()()()((()())())",
    "()((()))()",
    "()((())()()())()",
    "()()()()()()",
]

for test_case in tests:
    result = parse_nested_parens(test_case)
    assert len(result) == len(tests[0]), f"Error in test case: {test_case}"
    print(f"Test case: {test_case}")
    print(result)
```

This script defines a function `parse_nested_parens` that takes a string of parentheses and returns a list of the deepest level of nesting. The function uses a regex pattern to find all matches of parentheses and uses the `re.push()` method to stack the list items in the order of matches. Finally, the function returns the list of results.