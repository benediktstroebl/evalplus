```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opener, closer in zip('(()')[::-1], ')')[::-1]:
        stack = []
        level = 0
        for c in s:
            if c == opener:
                stack.append(opener)
                level += 1
            elif c == closer:
                if stack:
                    stack.pop()
                    level -= 1
                else:
                    result.append(level)
        if stack:
            result.append(level)
    return result
```

The code uses a simple approach that iterates through the input string and keeps track of nested parentheses by maintaining a stack and tallying the current nesting level. It then reverses the list of levels to ensure correct ordering and lastly, it returns the result. 

To verify its behavior against the provided test case, you can employ the following test case:
```python
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
``` 

To execute the test, run the `test_parse_nested_parens` function or incorporate it into a larger test suite.  This way, you can validate the functionality of the `parse_nested_parens` function and ensure it accurately solves the problem.