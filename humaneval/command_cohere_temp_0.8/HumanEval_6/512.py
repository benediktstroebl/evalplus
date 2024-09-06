```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        stack = []
        depth = 0
        for c in token:
            if c == '(':
                stack.append(c)
            else:
                if not stack or stack[-1] != '(':
                    result.append(depth)
                stack.pop()
                depth += 1
        if stack:
            result.append(depth)
    return result
```

The specified Python script solves the problem of parsing nested parentheses in a string and outputting the deepest level of nesting for each group separated by spaces.

The function `parse_nested_parens` takes a string `s` as input, which contains multiple groups of nested parentheses separated by spaces. It returns a list where each element represents the deepest level of nesting for the corresponding group. The deepest level of nesting is determined by tracking the parentheses on a stack and incrementing a `depth` counter whenever a closing parenthesis is encountered.

The script includes a `demo` example that tests the function with a sample string and compares the output with the expected result. The function's behavior is further validated with an `assert_equals` unit test that checks for the correct parsing of nested parentheses.