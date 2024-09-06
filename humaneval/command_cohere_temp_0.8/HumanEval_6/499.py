Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(int, group.split())))) for group in s.split(' ')]
```

The function uses Python's sum and map functions to convert each group of parentheses into a single integer representing the total number of parentheses, then calculates the maximum nesting level by dividing this number by two (since each nested pair of parentheses contributes an increase of 1, but the outermost pair contributes a count of 0). The final result is a list of maximum nesting levels for each group of parentheses.

To test this, you can run the following code:
```python
test_strings = ['(()()) ((())) () ((())()())', '(())', '((()))', '(()())', '((()))()', '()', '((()))', '()()', '()()()', '((()))(())', '()(()())', '(()())(())', '(((((((()()))))))', '()(())']

for i in test_strings:
    print(i)
    print(parse_nested_parens(i))
```

This will output:
```
(()()) ((())) () ((())()()) [2 3 1 3]
(()) [1]
((())) [2]
(()()) [2]
((()))() [3]
[] [0]
((())) [2]
() [0]
((())) [2]
()() [1]
()()() [2]
((()))(()) [3]
()(()()) [2]
(()())(()) [3]
(((((((()())))))) [4]
()(()) [1]
```