```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This code uses the swapcase function to convert alphabetic characters to their opposite case and leaves non-alphabetic characters unchanged. The result is a cleaned string with flipped cases. 

To verify the functionality, you can run the following commands:
```python
import unittest

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('HeLLo'), 'hELLo')
        self.assertEqual(flip_case('jima_P'), 'jIma_p')

if __name__ == '__main__':
    unittest.main()
```

Here, the `unittest` module is used to execute the test cases and verify the function's behavior. 

Note that this code assumes the existence of the `unittest` module, which is a built-in Python module used for testing. If you are using a Python environment that does not have `unittest` installed, you may need to install it separately. 

Let me know if you need help with anything!