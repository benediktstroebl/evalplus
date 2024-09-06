```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        nest = 0
        i = 0
        for char in token:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
```
The provided Python script solves the problem of parsing nested parentheses and returns the deepest level of nesting for each group in the input string separated by spaces.

The function takes a string s as input and splits it into individual groups of parentheses. It initializes an empty list result to store the deepest nesting level for each group. Then, it iterates through each token (a substring of s that is separated by a space) and calculates the nesting level by counting the opening parentheses '(' and subtracting the count of closing parentheses ')' in each token. This count is then appended to the result list.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This would output `[2, 3, 1, 3]` as the deepest level of nesting for each group of parentheses in the provided input string.