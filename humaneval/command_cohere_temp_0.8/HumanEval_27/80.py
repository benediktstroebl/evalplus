```python
def flip_case(string: str) -> str:
    return ''.join(char.swapcase() if char.isalpha() else char for char in string)
```

This code uses a list comprehension to iterate through each character in the input string. For alpha characters, it uses the `swapcase()` method to flip between uppercase and lowercase. Non-alpha characters are left unchanged. The final string is then rejoined after the modifications. 

To test this code, you can use the following markdown:
```
```python
import unittest

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('Hello'), 'hELLO')
    def test_flip_case_with_non_alphabetic_characters(self):
        self.assertEqual(flip_case('Hello, World!'), 'hELLO, wORLD!')

if __name__ == '__main__':
    unittest.main()
```
```
This code will ensure that the `flip_case` function behaves as expected. 

Let me know if I can help configure the tests or provide additional assistance.