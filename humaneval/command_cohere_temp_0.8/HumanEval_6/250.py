```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_bracs = segment.count('(')
        close_bracs = segment.count(')')
        result.append(open_bracs - close_bracs)
    return result
```

The `parse_nested_parens` function uses a simple approach to parse the input string. It counts the number of opening and closing parentheses for each segment (separated by spaces) and subtracts the closing parentheses from the opening ones to get the current level of nesting. The results are then collected in a list and returned. 

The unit tests are performed using Python's built-in `unittest` module. You can create a test case with the `TestCase` class and add individual test methods, each of which starts with the prefix `test`. Below is an example with two test cases; you can add more according to your needs:
```python
import unittest

class TestParseNestedParens(unittest.TestCase):

    def test_example_case(self):
        result = parse_nested_parens('(()()) ((())) () ((())()())')
        self.assertEqual(result, [2, 3, 1, 3])

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(""), [0])

    def test_single_group(self):
        result = parse_nested_parens("((()))")
        self.assertEqual(result, [2])

if __name__ == '__main__':
    unittest.main()
```