```python
def is_nested(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != brackets[char]:
                return False
    return not stack
```

The code works by first assuming that the string is correctly nested and using a stack to simulate the stack of brackets. Then, it iterates through the string, pushing each '('', '{', or '[' into the stack. It corresponds to an opening bracket, and when a corresponding closing bracket is encountered, it is checked if the last element in the stack is its matching opening bracket. If not, the string is not correctly nested. Finally, if the stack is empty at the end of the loop, the string is considered valid. 

The given example cases demonstrate various inputs and expected outputs. Feel free to uncomment them and replace the placeholder with your own problem cases to test the function. 
```python
# test_is_nested.py
import unittest
from is_nested import is_nested

class TestIsNested(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertTrue(is_nested('[[[]]]'))
        self.assertTrue(is_nested('[]'))
        self.assertTrue(is_nested('{}'))
        self.assertTrue(is_nested('()'))
        self.assertTrue(is_nested('[]{}()[]'))

    def test_invalid_inputs(self):
        self.assertFalse(is_nested('][]'))
        self.assertFalse(is_nested('][]'))
        self.assertFalse(is_nested('([])'))
        self.assertFalse(is_nested('{[]}'))
        self.assertFalse(is_nested('[[]))'))

if __name__ == '__main__':
    unittest.main()
```
Please feel free to customize the test cases according to your problem statement and add more cases to cover edge scenarios if necessary.