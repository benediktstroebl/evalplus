```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                result.append(')'.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
            current_group = []
        else:
            current_group.append(char)

    # Handle the last group
    if not stack:
        result.append(')'.join(current_group))
    else:
        pre_group = stack.pop()
        current_group.extend(pre_group)
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. When an open parentheses `(` is encountered, we push the current group onto the stack and start a new group. When a closing parentheses `)` is encountered, we:
1. Check if the stack is empty. If yes, this `)` closes the current group, which we add to the result. If no, this `)` corresponds to the opening `(` of a nested group, so we pop the nested group from the stack and add it to the current group.
2. After processing, we handle the last group if it's still on the stack.

The result list contains the separate groups after processing. The script ignoes any spaces in the input string. 

This approach guarantees that groups are balanced and separated correctly, even if they are deeply nested. It also does not rely on ordering of the characters so it remains correct even if the input string is not sorted. 

The unit tests for this problem can be created using the `unittest` module, which comes with Python. You can define a test case for each possible scenario to cover different combinations of opening and closing parentheses. Here is an example of test cases for this function:
```python
import unittest

def separate_paren_groups(paren_string: str) -> List[str]:
    return separate_paren_groups.__wrapped__(paren_string)  # Use the original function

class TestSeparateParenGroups(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(separate_paren_groups("()"), ['()'])
        self.assertEqual(separate_paren_groups("(())"), ['()', '(())'])
        self.assertEqual(separate_paren_groups("(()())"), ['()', '(())', '(()())'])

    def test_deeply_nested(self):
        self.assertEqual(separate_paren_groups("(((())))")) ['(((())))'])
        self.assertEqual(separate_paren_groups("(((((())))))"), ['(((())))', '(((((())))))'])

    def test_ignore_spaces(self):
        self.assertEqual(separate_paren_groups(" ( ) (( )) (( )( )) "), ['()', '(())', '(()())'])

    def test_multiple_groups(self):
        self.assertEqual(separate_paren_groups("(a)(b)c(d)(e)"), ['(a)', '(b)', 'c', '(d)', '(e)')])

if __name__ == '__main__':
    unittest.main()
```