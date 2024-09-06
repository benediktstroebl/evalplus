```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension to multiply each number in the array by the following number's sign, and then sum these products together. It returns None for an empty array as requested.

Here is a snippet of code you can use to test this function:
```python
import unittest

class TestProdSigns(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)
```
This code will run the `prod_signs` function with the input [1, 2, 2, -4], [0, 1], and [] and compare the result with -9, 0, and None respectively.  It is important to note that you should run this code with a Python interpreter that has the `prod_signs` function available. If you are using an environment like GitBash, make sure to adjust the interpreter accordingly.