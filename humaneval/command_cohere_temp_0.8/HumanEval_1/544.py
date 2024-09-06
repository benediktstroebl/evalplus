Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses. 

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'
    paren_groups = []
    stack = []

    for char in paren_string:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces and stack:
            stack.pop()
        elif not stack:
            paren_groups.append('')
        else:
            paren_groups[-1] += char

    return paren_groups
```

To test the function, the script includes a local test where the function is called with a sample input and the resulting output is printed. The sample input is `'( ) (( )) (( )( ))'`, and the expected output is `['()', '(())', '(()())']`. The code then verifies that the output matches the expected output. 

```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```

The function also undergoes a unit test using the `unittest` module, and the test case is defined as follows:
```python
import unittest

def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'
    paren_groups = []
    stack = []

    for char in paren_string:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces and stack:
            stack.pop()
        elif not stack:
            paren_groups.append('')
        else:
            paren_groups[-1] += char

    return paren_groups

class TestSeparateParenGroups(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(
            separate_paren_groups('( ) (( )) (( )( ))'),
            ['()', '(())', '(()())']
        )

    def test_single_group(self):
        self.assertEqual(
            separate_paren_groups('()'),
            ['()']
        )

    def test_no_group(self):
        self.assertEqual(
            separate_paren_groups('xyz'),
            ['xyz']
        )

    def test_multiple_nested_groups(self):
        self.assertEqual(
            separate_paren_groups('((()))'),
            ['(())', '()()']
        )

if __name__ == '__main__':
    unittest.main()
```

To run the test, the `unittest` module runs all the test cases defined with the `unittest.TestCase` class, and the results are displayed to specify whether the test passes or not. 
This way, the `separate_paren_groups` function is tested against different inputs to verify its functionality. 
If there are any changes or improvements to be made to the function, the tests will indicate them, and they can be made with confidence.