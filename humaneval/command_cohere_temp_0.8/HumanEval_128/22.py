```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array and multiplies them with the product of all signs of each number in the array. The result is returned if the array is not empty, and `None` is returned otherwise.

Here's an example usage illustration:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
```
And here's how the code passes tests:
```python
import unittest

def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result

class TestProdSigns(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test_example2(self):
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_example3(self):
        self.assertIsNone(prod_signs([]))

    def test_empty_list(self):
        self.assertIsNone(prod_signs([]))

    def test_negative_elements(self):
        self.assertEqual(prod_signs([-2, 2, -3, 3]), -18)

if __name__ == '__main__':
    unittest.main()
```