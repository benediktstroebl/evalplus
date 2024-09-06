```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script defines a function `flip_case` that takes a string as an argument and flips the case of alphabetic characters, leaving non-alphabetic characters unchanged. It uses the `swapcase` method to invert the case of alphabetic characters, and the `join` method to concatenate the modified characters back together.

To test this, you can run the following Python code:
```python
import unittest

def test_flip_case():
    # Test string with alphabetic characters in different cases
    assert flip_case('Hello World') == 'hELLO WORLD'

    # Test string with non-alphabetic characters
    assert flip_case('123 $% Hello') == '123 $% hELLO'

    # Test empty string
    assert flip_case('') == ''

if __name__ == '__main__':
    unittest.main()
```

This will run the `test_flip_case` function and its assertions, confirming that the `flip_case` function works as expected.