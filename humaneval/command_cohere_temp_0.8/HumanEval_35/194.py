```python
def max_element(l: list) -> int:
    """Return maximum element in the list.
    
    Args:
        l (list): List of elements.
        
    Returns:
        int: Maximum element in the list.
    """
    return max(l)
```

This script defines a function `max_element(l)` that takes a list `l` as an input and returns the maximum element in the list using the `max()` function. This function is used to find the maximum element in the list specified in the function arguments. 

The tests were not provided, but the function should pass the tests for the provided examples in the prompt. 
If you want to test this function, you can use the following sample tests:
```python
test_max_element_valid = [(>[1, 2, 3], 3), 
                         ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 123)]
```

```python
import unittest

class TestMaxElementFunction(unittest.TestCase):
    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_max_element_complex(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()
```

In the above code, `TestMaxElementFunction` is a test class with two test methods: `test_max_element` and `test_max_element_complex`. Each test method verifies whether the `max_element()` function returns the expected maximum value for the given input. 

You can run this test file to verify that the `max_element()` function passes both tests. 
If the tests pass, it means the function correctly finds the maximum element in the given lists.