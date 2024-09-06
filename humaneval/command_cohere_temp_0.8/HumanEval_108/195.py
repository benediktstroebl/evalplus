```python
def count_nums(arr):
    output = sum(int(n) for n in arr if sum(int(d) for d in str(n)) > 0)
    return output
```
This function sums over all elements in the input array `arr`. For each element n, it checks if the sum of its digits is greater than 0. This is done using a generator expression `(d for d in str(n))`, where each `d` is a digit, and `str(n)` converts the element n to a string. If the sum of these digits is greater than 0, it adds 1 to the total count, otherwise, it does nothing, as stated in the ternary operation `if sum(int(d) for d in str(n)) > 0`. Finally, it returns this total count. 

The unit tests stated in the problem are taken care of by the built-in Python test framework, `unittest`. These tests are defined below:
```python
import unittest

class TestCountNums(unittest.TestCase):
    def test_count_nums_empty_array(self):
        self.assertEqual(count_nums([]), 0)

    def test_count_nums_array_with_positive_digits(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_count_nums_array_with_negative_digits(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)


if __name__ == '__main__':
    unittest.main()
```
In the code above, `test_count_nums_empty_array`, `test_count_nums_array_with_positive_digits`, and `test_count_nums_array_with_negative_digits` are individual test cases defined as functions within the `TestCountNums` class, which is a subclass of `unittest.TestCase`. They take assertions stated in the problem and incorporate them into `self.assertEqual()` which checks if two arguments are equal; if they are not, the test fails. 

The `unittest.main()` call runs the tests and collects the results, which are then printed to the console. 
To execute this test suite, you can run the script file with Python, and the results will be displayed on the console: 
```bash
$ python script_name.py
```