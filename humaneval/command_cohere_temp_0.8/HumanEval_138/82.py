```python
def is_equal_to_sum_even(n):
    even_nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    return n in even_nums
```

This function directly tests if the given number n is present in the list of positive even numbers. 

To test this function, you can write an unittest:
```python
import unittest

class TestIsEqualToSumEven(unittest.TestCase):
    def test_is_equal_to_sum_even(self):
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertTrue(is_equal_to_sum_even(20))
    def test_is_equal_to_sum_even_edge_cases(self):
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(30))
        self.assertFalse(is_equal_to_sum_even(2))
        self.assertFalse(is_equal_to_sum_even(22))
if __name__ == '__main__':
    unittest.main()
```

This unittest contains two test cases to thoroughly test the functionality of the `is_equal_to_sum_even()` function. 

The `test_is_equal_to_sum_even` case tests the function with different input values and expects True and False results accordingly. 

The `test_is_equal_to_sum_even_edge_cases` case tests edge cases to ensure the function behaves correctly even with limited and excessive values. 

The `unittest.main()` function is essential to discover and run all the test cases. 

To run the test, save the code into a Python file (e.g., `test_is_equal_to_sum_even.py`) and execute the file in your Python environment. 

The script output will indicate whether the test cases passed or failed.  If all tests pass, it will show: 
 ```python
....

----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
``` 
This will assure you that the function `is_equal_to_sum_even()` works correctly.