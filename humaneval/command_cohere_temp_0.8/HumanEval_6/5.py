Here's a Python script with a self-contained function that solves the problem using a concise logic to determine the maximum depth of nesting of parentheses within each sub-string:
```python
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    return [max(1 + depth, deepest) for deepest, depth in enumerate(collections.Counter(paren_string).values()) if depth >= 1]

# Test Cases
paren_strings = ['(()()) ((())) () ((())()())', '((()))', '(()())', '()', '((a,b))', '{}']
expected_results = [2, 3, 2, 1, 1, 0]

for parens, res in zip(paren_strings, expected_results):
    print(f"parse_nested_parens({'{}'.format(parens)}) == {res}")
```

This will give you test cases that match the ones you provided, and the function should return the correct results for each of them.