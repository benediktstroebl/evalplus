```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nest in s.split():
        depth = 0
        i = 0
        while i < len(nest):
            if nest[i] == '(':
                depth += 1
            else:
                depth -= 1
            i += 1
        result.append(depth)
    return result
```
The function splits the string into a list of strings based on spaces, and then for each substring, it counts the number of '(' and ')' to determine the deepest level of nesting of parentheses. The output is a list that contains the deepest level of nesting for each string. 
The unit test for this function can be added based on the given test case like this:
```python
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
``` 
The test code checks if the output of the function corresponds to the expected result. 
To run the test, you can add this code before the function definition and run the script:
```python
import unittest

class TestParseNestedParens(unittest.TestCase):
    def test_parse_nested_parens(self):
        assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
``` 
The `unittest` module is used to define a test class with a single test method, `test_parse_nested_parens`, which calls the function and checks if the output is as expected. 
When the script is run, the test case will be executed, and if everything is correct, you should not see any error messages and everything will run smoothly.