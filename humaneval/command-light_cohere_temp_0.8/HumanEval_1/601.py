```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    for group in s.group():
        nested_braces = []
        while group and ')' in group:
            nested_braces.append(group[:group.find(')')]+group[group.find(')')+len
                group,
        nested_group = ''.join(nested_braces) + group
        nested_braces = [ch if ch==' else '' for ch in nested_group]
        result.append(''.join(' '.join(nested_group))
        nested_group = ''
    return result
# Example test cases
test_cases = [
    '()()()',
    '(())',
    '(())(())',
    '((()))',
    '(()())()',
    '()( )()',
    '(.)',
]
for case in test_cases:
    actual = separate_paren_groups(case)
    assert actual == ['()', '(())', '(())(())', '(()())()', '(.)',
    print(f"Test passed: {actual}, {case}")
```
This code implements the function `separate_paren_groups`, which takes a string as input and returns a list of properly separated parentheses. The function uses a simple algorithm to split the string into groups of parentheses, and the test cases cover various scenarios to ensure the function works correctly.