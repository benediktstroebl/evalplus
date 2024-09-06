```python
def prod_signs(arr):
    result = None
    if arr:
        arr_signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
        result = sum([abs(i) for i in arr]) * prod(arr_signs)
    return result
```
This function calculates the magnitude of each number in the array and identifies the signs of each number (1, -1, or 0), then multiplies the magnitudes together and the signs respectively and returns the appropriate sum. 

Here are some test cases to ensure the function behaves as expected:
```python
import unittest

class TestProdSigns(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)

    def test_prod_signs_with_negative_numbers(self):
        self.assertEqual(prod_signs([-3, -2, 2]), 12)

    def test_prod_signs_with_zero(self):
        self.assertEqual(prod_signs([0, 0, -2, 0]), 0)

    def test_prod_signs_with_only_zero(self):
        self.assertEqual(prod_signs([0, 0, 0]), 0)

    def test_prod_signs_with_negative_and_positive(self):
        self.assertEqual(prod_signs([-3, 2, -5, 2]), 15)

    def test_prod_signs_with_large_numbers(self):
        self.assertEqual(prod_signs([1234, -5678, 2344, -9011]), -4053662)

if __name__ == '__main__':
    unittest.main()
```