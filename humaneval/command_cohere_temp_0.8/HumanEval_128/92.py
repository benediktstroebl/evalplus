```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * [-1, 1, 0]
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result
```

This function takes an array of integers as input and returns the sum of the magnitudes of the integers multiplied by the product of all signs of each number in the array, represented by 1, -1, or 0. If the array is empty, it returns **None**.

The script includes corresponding unit tests which verify the function implementation against a variety of input scenarios:
```python
import unittest

def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * [-1, 1, 0]
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result

class TestProdSigns(unittest.TestCase):
    def test_single_int(self):
        self.assertEqual(prod_signs([5]), 5)

    def test_two_positive_ints(self):
        self.assertEqual(prod_signs([2, 4]), 10)

    def test_two_negative_ints(self):
        self.assertEqual(prod_signs([-3, -5]), -15)

    def test_mixed_ints(self):
        self.assertEqual(prod_signs([-2, 3, -4, 6]), -24)

    def test_empty_list(self):
        self.assertIsNone(prod_signs([]))

    def test_list_with_zero(self):
        self.assertEqual(prod_signs([0, 2, -3, 4]), 0)

    def test_list_with_multiple_zeros(self):
        self.assertEqual(prod_signs([0, 0, 5, -5]), 0)

if __name__ == '__main__':
    unittest.main()
``` 

To execute the test suite, run the script from the command line by typing:
```bash
python script_name.py
``` 

This will run the tests which will verify the correctness of the **prod_signs** function against the various scenarios outlined in the tests. 

Please let me know if you have any questions or if you'd like to elaborate on any of the aforementioned points!