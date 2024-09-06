```python
def unique_digits(x):
    odd = [int for int in x if any(int % 2 for int in str(int))]
    return sorted(odd)
```

The solution works by using a list comprehension that generates a list of odd integers from the list of provided integers. Subsequently, the `any()` function utilizes the `int % 2` expression for each integer to determine whether the number possesses an even digit, and filters out the even digits. Lastly, the function returns a sorted list of the odd integers.

The test cases can be easily created using Python's built-in `unittest` module. Here is an example:
```python
import unittest

class TestUniqueDigits(unittest.TestCase):
    def test_unique_digits_example1(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])

    def test_unique_digits_example2(self):
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_unique_digits_example3(self):
        self.assertEqual(unique_digits([21, 43, 39, 74, 61]), [21, 43, 61, 74])

if __name__ == '__main__':
    unittest.main()
```

In the test script, the `unittest` module is utilized to create three distinct test cases. For each test case, the predefined `assertEqual()` function is used to compare the output of the `unique_digits()` function with the anticipated outcome. The `if __name__ == '__main__'` statement ensures that the test suite is executed when the script is run directly. 

To execute the script, save it as a `.py` file and run it using a Python interpreter. The test suite will be executed, and any failures or errors will be reported. To focus on a specific test case, add the argument `-k` followed by the name of the test case you want to focus on, like `-k test_unique_digits_example1`.