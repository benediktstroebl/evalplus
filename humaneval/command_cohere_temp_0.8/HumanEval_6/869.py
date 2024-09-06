```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), s.split())))) for _ in range(len(s.split()))]
```

The provided code employs a list comprehension and the `max` function to derive the maximum depth of parentheses nesting for each group in the input string.

The function can be tested as follows:
```python
import unittest

class TestDeepestLevel(unittest.TestCase):
    def test_single_paren(self):
        self.assertEqual(parse_nested_parens("(()())"), [2])

    def test_double_paren(self):
        self.assertEqual(parse_nested_parens("(((()())))"), [3])

    def test_mixed_paren(self):
        self.assertEqual(parse_nested_parens("(()()) ((()))"), [2, 3])

    def test_nested_with_space(self):
        self.assertEqual(parse_nested_parens("(()()) () ((())()())"), [2, 3, 1, 3])

if __name__ == '__main__':
    unittest.main()
```

This test suite contains four test functions (`test_single_paren`, `test_double_paren`, `test_mixed_paren`, and `test_nested_with_space`) which cover various scenarios. When the `unittest.main()` function is executed, it automatically runs all the test functions.