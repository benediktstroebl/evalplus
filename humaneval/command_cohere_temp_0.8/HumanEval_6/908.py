```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        nesting = 0
        level = 0
        for c in token:
            if c == '(':
                nesting += 1
            else:
                nesting -= 1
            level = max(level, nesting)
        result.append(level)
    return result
```

This script includes the function `parse_nested_parens()` that takes a string as input and returns a list of the maximum nesting level of parentheses in each token. The maximum nesting level is calculated by maintaining a count of left parentheses (`('`)`) and subtracting a count of right parentheses (`(')``) in each token. The maximum of this count at any point in the loop becomes the nesting level for that token. This process is then repeated for each token in the input string, and the resulting list of nesting levels is returned. 

To test this, we can create a simple test case using the `pytest` framework, which is already included in the code snippet below:
```python
def test_parse_nested_parens():
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    assert result == [2, 3, 1, 3]
```

This will ensure that the function `parse_nested_parens()` produces the expected output for the provided test case.