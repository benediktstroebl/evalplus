```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script uses Python's array filtering functionality and the & operator to find the intersection of the two arrays (oddFirsts and oddLasts). Length of the resulting array corresponds to the number of elements that satisfy the problem condition. 

To test this script, you can create a unittest module or use Python's built-in `unittest` testing framework. You can create a test case that passes a list of numbers to the `specialFilter` function and assert that the output is correct. Here is an example: 
```python
import unittest

def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)

class TestSpecialFilter(unittest.TestCase):
    def test_example(self):
        self.assertEqual(specialFilter([15, -73, 14, -15, 33, -2, -3, 45, 21, 109]), 1)
        self.assertEqual(specialFilter([21, 109, 505, 719, 957, 785, 649, 753, 891, 531]), 3)
        self.assertEqual(specialFilter([217, 326, 655, 457, 896, 190, 994, 752, 713, 719]), 2)
        self.assertEqual(specialFilter([-11, -8, -555, -1, -18, -525, -931, -118, -945, -619]), 2)

    def test_empty_list(self):
        self.assertEqual(specialFilter([]), 0)

    def test_single_number(self):
        self.assertEqual(specialFilter([123]), 0)

if __name__ == '__main__':
    unittest.main()
```

This unittest contains four test functions that test the `specialFilter` function on various inputs: 
 - `test_example`: These tests verify the correctness of the `specialFilter` by comparing the length of the resulting array with the expected output for three different inputs.
 - `test_empty_list`: This test verifies that the function returns 0 when an empty list is passed to the `specialFilter` function.
 - `test_single_number`: This test case verifies that the function returns 0 when a list with a single number is passed. 

You can safely add more tests to this unittest to further verify the correctness of the `specialFilter` function. 

To run the tests, you can save the `unittest` module in a file (e.g., `test_special_filter.py`) and run the script in your command line via `python -m unittest test_special_filter`. 

This command will run the `unittest` and report on the number of tests passed. 

I hope this helps explain how to create robust test suites in Python. Let me know if you have any further questions!