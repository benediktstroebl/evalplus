```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        level = 0
        nesting_level = 0
        for c in token:
            if c == '(':
                nesting_level += 1
            elif c == ')':
                nesting_level -= 1
            else:
                pass
            level = max(level, nesting_level)
        result.append(level)
    return result
```

The code uses a straightforward iterative strategy to examine each token (substring with nested parentheses) in the input string individually. It keeps track of the overall nesting level `level` and the current nesting level `nesting_level` for each token. When it encounters a '(', the `nesting_level` is increased, and when it encounters a ')', the `nesting_level` is decreased. The `level` is updated with the maximum nesting level reached while traversing the token. This process is repeated for each token, and the deepest level of nesting for each token is stored in the `result` list.

The unit test based on the provided example input is also included in the script:
```python
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
```

The test case uses Python's `assert` statement to validate if the output of the `parse_nested_parens` function matches the expected result. The `parse_nested_parens` function is called with the specified input, and the result is compared to the expected output. If the values match, the test passes, confirming that the function works correctly. 

This function can efficiently handle the specified problem and provide a list of integer values, representing the deepest nesting level for each group of parentheses in the input string.