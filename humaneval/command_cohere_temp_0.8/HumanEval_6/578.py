```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        depth = 0
        imbalance = 0
        for char in segment:
            if char == '(':
                depth += 1
                imbalance += 1
            elif char == ')':
                depth -= 1
                imbalance -= 1
        result.append(depth)
    return result
```
The function iterates through each segment of the string and maintains a `depth` variable to track the current nesting level. When a left parenthesis is encountered, the `depth` is incremented and an `imbalance` counter is increased to keep track of the difference between the number of opening and closing parentheses. When a right parenthesis is encountered, the `depth` is decremented and the `imbalance` counter is decreased. The function returns a list of these maximum depths of nesting for each segment.

Here is a simple test script to verify the functionality of the function:
```python
def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("()") == [1]
    assert parse_nested_parens("(((((()()))))))")) == [4]
    assert parse_nested_parens("(()())") == [2]

test_parse_nested_parens()
```