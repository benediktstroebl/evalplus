```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)
```

This code uses a list comprehension with a conditional to determine whether each character of the string should be flipped to its flipped case or remain the same based on its current case. The resulting string is then returned as the result of the function. 

To test this code, you can run the following:
```python
import unittest

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('HeLLo'), 'hELLo')
        self.assertEqual(flip_case('hipPiT'), 'hIPPiT')
    def test_flip_case_empty_string(self):
        self.assertEqual(flip_case(''), '')
    def test_flip_case_mixed_case(self):
        self.assertEqual(flip_case('HeLiO'), 'hELiO')

if __name__ == '__main__':
    unittest.main()
```

This tests the `flip_case` function with a variety of inputs: `HeLLo` to ensure flipiness, `hipPiT` to ensure uppiness, `HeLiO` to ensure mixed case flipiness, and an empty string to ensure that an empty string doesn't break the function. The `unittest.main()` call runs the tests if the script is executed directly. 

This code should provide a straightforward and effective way to flip the case of characters within a string.