Here's a Python script with a self-contained function that solves the problem using a concise and efficient approach:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(nesting, 1 if char in '(){}' else 0)
            for char, nesting in enumerate(zip(*[iter(s)] * 2), 1)]
```

This approach uses a generator expression and the `enumerate` function to calculate the nesting level of each opening parenthesis, updating the nesting level based on the corresponding closing parenthesis and the characters between them. The maximum nesting level is computed for each group and returned as a list.

The unit tests provided in the problem statement can be tested using Python's built-in `unittest` module. Here's how you can test the function using `unittest`:
```python
import unittest

from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(nesting, 1 if char in '(){}' else 0)
            for char, nesting in enumerate(zip(*[iter(s)] * 2), 1)]

class TestParseNestedParens(unittest.TestCase):
    def test_example(self):
        result = parse_nested_parens('(()()) ((())) () ((())()())')
        self.assertEqual(result, [2, 3, 1, 3])

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(''), [0] * 10)

    def test_single_group(self):
        self.assertEqual(parse_nested_parens('()'), [1])

    def test_multiple_groups(self):
        test_strings = [
            '(()())',
            '((()))',
            '(()()) () ((())())',
            '(()()) ((()))',
            '(((()())))',
            '(()()) ()',
            '()',
            '((()))',
            '() ()',
            '()',
            '() () ()',
            '(()())(())'
        ]
        expected_results = [2, 3, 2, 3, 3, 2, 1, 0, 2, 1, 3, 1]
        for test_str, expected in zip(test_strings, expected_results)):
            with self.subTest(test_str=test_str):
                self.assertEqual(parse_nested_parens(test_str), expected)

if __name__ == '__main__':
    unittest.main()
```

This script will run the `unittest` tests and report any failures or errors. It's a way to systematically test your function against various scenarios and ensure it behaves as expected.