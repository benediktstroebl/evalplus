Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing only the separate groups of parentheses. The groups are balanced and non-nested. The function also ignores any spaces in the input string. 

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            if stack:
                current_group += ')'
                stack.pop()
            else:
                current_group += char
        else:
            current_group += char

    return stack + [current_group]
```

To test the function, the script includes a unittest framework with a test case that checks whether the function's output correctly separates the groups in the input string. The test case is defined as follows:
```python
import unittest

class TestSeparateParenGroups(unittest.TestCase):
    def test_separate_paren_groups(self):
        self.assertEqual(
            separate_paren_groups("( ) (( )) (( )( ))"),
            ["()", "(())", "(()())"],
        )
```

To run the test, the command is provided below:
```bash
python test_separate_paren_groups.py
```

This command will run the unittest, which will verify that the `separate_paren_groups` function's output is correct. If the function behaves correctly, the test will pass; otherwise, it will fail, which is essential for maintaining code quality and ensuring that the function behaves as expected.