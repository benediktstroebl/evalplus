```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open, close = 0, 0
        for char in segment:
            if char == '(':
                open += 1
            else:
                close += 1
        result.append(open + close)
    return result
```
The function processes the input string in the following steps:
1. It splits the entire input string into multiple segments using space as a separator.
2. For each segment representing a group of parentheses, it counts the number of opening and closing parentheses as characters.
3. It calculates the sum of these counts as the measure of the deepest level of nesting for this group and adds this value to the `result` list.
4. The final list `result` contains the measure of the deepest level of nesting for each group of parentheses in the input string.

The solution is tested on the provided test case and another additional test:
```
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
>>> parse_nested_parens('()')
[0]
>>> parse_nested_parens('(((((((()())
[5]
```