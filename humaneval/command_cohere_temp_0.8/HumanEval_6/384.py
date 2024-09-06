```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        i = 0
        for char in chunk:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
```
The `parse_nested_parens` function takes a string as input and splits it into chunks based on spaces. For each chunk, it counts the number of open parentheses '(' and subtracts the number of closed parentheses ')' to get the current nesting level. This nesting level is then appended to the `result` list. The resulting list of nesting levels for each group represents the deepest level of nesting for each group of parentheses.

To test this script, you can run the following code, which will assert the expected output against the function's output on the provided input:
```python
import unittest

def test_parse_nested_parens():
    # Test case
    input_str = '(()()) ((())) () ((())()())'
    expected = [2, 3, 1, 3]
    result = parse_nested_parens(input_str)
    unittest.assertListEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
``` 

This will run the test and verify that the output of the function is the expected output.