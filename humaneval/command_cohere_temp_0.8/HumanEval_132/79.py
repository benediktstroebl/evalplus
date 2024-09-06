```python
def is_nested(s):
    open, closed = 0, 0
    for char in s:
        if char == '[':
            open += 1
        elif char == ']':
            closed += 1
        if open > closed:
            return False
    return open != closed
```

The function counts the opening and closing brackets respectively whenever it encounters a '[' or a ']' character. Whenever there is a mismatch between the opening and closing brackets, the function returns `False`. Otherwise, if the counts are not equal, it means there is at least one nested bracket in the sequence and the function returns `True`. 

Here is a unittest with examples from the problem description: 
```python
class TestIsNested(unittest.TestCase):
    def test_is_nested_valid1(self):
        self.assertTrue(is_nested('[[[]]]'))

    def test_is_nested_valid2(self):
        self.assertTrue(is_nested('[][]'))

    def test_is_nested_valid3(self):
        self.assertTrue(is_nested('[][][]'))

    def test_is_nested_invalid1(self):
        self.assertFalse(is_nested('[][]'))

    def test_is_nested_invalid2(self):
        self.assertFalse(is_nested('[]'))

    def test_is_nested_invalid3(self):
        self.assertFalse(is_nested('[]]]'))

    def test_is_nested_invalid4(self):
        self.assertFalse(is_nested('[][][][]'))

    def test_is_nested_invalid5(self):
        self.assertFalse(is_nested('[[[]'))

    def test_is_nested_invalid6(self):
        self.assertFalse(is_nested(']]][[[[]'))

if __name__ == '__main__':
    unittest.main()
```

This unittest contains examples from the problem description and tests the functionality of our function. It can be run by executing the `unittest` command in the script. 

Note: this script assumes that the function `is_nested` is defined in a file called `test_is_nested.py` and that the unittest is defined with the class `TestIsNested`. If you would like to run this script with a different name or in a different file, you may need to adjust the script accordingly.