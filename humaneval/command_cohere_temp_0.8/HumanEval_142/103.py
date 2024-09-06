```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The code uses a for loop to iterate through each index and number in the provided list. By using the `enumerate` function, the code can easily reference the index of each number. If the index is a multiple of 3, the number is squared; if the index is a multiple of 4 but not 3, the number is cubed. The sum of all numbers is then returned. 

To ensure the effectiveness of this code, you may want to consider adding tests, such as the ones provided in the original problem. These tests can be added to a separate file with the `.test` extension, and you can use Python's `unittest` framework to check if the function behaves as expected. 

For example, you could create a `test_sum_squares.test` file with the following content:
```python
import unittest
from sum_squares import sum_squares # assuming the script with your function is in a file named sum_squares.py

class TestSumSquares(unittest.TestCase):
    def test_sum_squares_example1(self):
        self.assertEqual(sum_squares([1, 2, 3]), 6)

    def test_sum_squares_example2(self):
        self.assertEqual(sum_squares([]), 0)

    def test_sum_squares_example3(self):
        self.assertEqual(sum_squares([-1, -5, 2, -1, -5]), -126)
    # add more tests as needed for other edge cases

if __name__ == '__main__':
    unittest.main()
```

This file creates a test class that executes the `sum_squares` function on different inputs and checks if the output matches the expected value. 

To run the tests, you can simply execute the test file using the Python interpreter:
```bash
python test_sum_squares.test
```

If all the tests pass, the output will be empty. If there is a failure, the output will indicate which test failed and why. 

This way, you can ensure that the function works correctly for different scenarios.