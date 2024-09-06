```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_group in s.split():
        stack = []
        depth = 0
        for char in bracket_group:
            if char == '(':
                stack.append(depth)
                depth += 1
            else:
                if not stack or stack.pop() > depth:
                    depth -= 1
                else:
                    depth += 1
        result.append(depth)
    return result
```

To test the function, the script includes a test case that verifies the function's behavior against a known output. The test is structured using Python's built-in `assert` statement:
```python
test_cases = ['(()()) ((())) () ((())()())', '(()')+'x'+')', '()()', '(((((((()())

for case in test_cases:
    expected = [2, 3, 1, 3]
    assert parse_nested_parens(case) == expected
```

The `assert` statement checks if the output of the `parse_nested_parens` function for each input in `test_cases` matches the corresponding element in `expected`. If the tests pass, the output will include a passage indicating that the tests completed successfully. If any test fails, the output will include the name of the test that caused the failure, which makes it easy to identify and rectify any issues in the function.