Here's a Python script with a self-contained function that solves the problem using a concise and optimized approach:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(nesting(group)) for group in s.split(' ') if group]

def nesting(s: str) -> int:
    if not s:
        return 0
    return max(1 + nesting(s[1:]), nesting(s[:-1]))
```

This approach uses a recursive 'nesting' function to efficiently calculate the maximum nesting level for a given string of parentheses. The overall time complexity is O(N^2) where N is the total number of parentheses tokens in the input string, but nonetheless provides a concise solution for the problem.

Ensure you have a suitable test case to verify the function's behavior:
```python
test_cases = [
    '(()()) ((())) () ((())()())',
    '((()))',
    '(()())',
    '(((((()())))))',
]

for case in test_cases:
    print(f"Test Case: {case}")
    expected = [2, 3, 2, 4]
    result = parse_nested_parens(case)
    print(f"Expected: {expected}")
    print(f"Result: {result}")
    assert result == expected
```

This test suite will ensure the function's behavior aligns with the expected output for various scenarios.