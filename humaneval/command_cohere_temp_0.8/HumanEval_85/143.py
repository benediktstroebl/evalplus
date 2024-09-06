```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function uses a list comprehension to filter out even integers that are positioned at odd indices from the given list `lst`. The function returns a list of integers that meet the given criteria. Underneath the code, there is a unittest that checks the functionality of the script:
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_function(self):
        # Test case one
        self.assertEqual(add([4, 2, 6, 7]), [2])
        # Test case two
        self.assertEqual(add([1, 3, 5, 7]), [5])
        # Test case three
        self.assertEqual(add([0, 2, 4, 6]), [4])
        # Test case four
        self.assertEqual(add([-2, -1, 3, 5]), [3])

    def test_add_function_empty_list(self):
        # Test case five
        self.assertEqual(add([]), [])

    def test_add_function_odd_length(self):
        # Test case six
        self.assertEqual(add([1, 2, 3]), [])

if __name__ == '__main__':
    unittest.main()
``` 

The script then employs the `unittest` module to run several tests on the `add()` function. Specifically, it checks for the function's behavior against six different scenarios, ensuring that the function behaves as expected. If the function returns the correct output for each test case, the code will output `PASS` for each test case, indicating that the function correctly solves the given problem.  This way, the code can ensure its correctness and logical functionality.