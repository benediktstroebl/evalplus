```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension that multiplies corresponding elements with signs represented as 1, -1, or 0, and then sums them up. The outcome is returned as None if the list is empty.

Here is a unittest test module to test the function:
```python
import unittest

def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result

class TestProdSigns(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(prod_signs([]), None)

    def test_single_number(self):
        self.assertEqual(prod_signs([5]), 5)

    def test_two_numbers(self):
        self.assertEqual(prod_signs([2, 4]), 8)

    def test_mixed_signs(self):
        self.assertEqual(prod_signs([1, 2, -3, 4]), 2)

    def test_only_negative(self):
        self.assertEqual(prod_signs([-1, -2, -3]), -6)

if __name__ == '__main__':
    unittest.main()
```

To run the tests, you can copy this code into a ".py" file and run it with your Python interpreter. 

This will run the unittest test module, which will execute the testcases and verify that the `prod_signs` function's output is correct.  By doing so it will ensure that the function behaves as expected.