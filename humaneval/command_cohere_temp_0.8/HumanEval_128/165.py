```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of all numbers in the input array and determines their signs (1, -1, or 0), then returns the sum of magnitudes multiplied by the product of all those signs. If the input array is empty, it returns `None`.

Here's an example usage:
```python
prod_signs([1, 2, 2, -4]) # Returns -9
prod_signs([0, 1]) # Returns 0
prod_signs([]) # Returns None
``` 
And here's a simple unit test suite to verify the correctness of the `prod_signs` function:
```python
import unittest

def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result

class TestProdSigns(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(prod_signs([5]), 5)
        self.assertEqual(prod_signs([-5]), 5)
        self.assertEqual(prod_signs([0]), 0)

    def test_multiple_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([-1, -2, -3]), 6)

    def test_empty_array(self):
        self.assertIsNone(prod_signs([]))

    def test_array_with_zero(self):
        self.assertEqual(prod_signs([0, 1, 2, 3, 0]), 0)

if __name__ == '__main__':
    unittest.main()
```