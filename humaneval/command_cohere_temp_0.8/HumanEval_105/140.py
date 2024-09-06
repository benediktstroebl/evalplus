Here's a Python script that implements the `by_length` function and demonstrates how to test it using unittest:
```python
import unittest

def by_length(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted_arr[::-1]
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(NUMBER_TO_NAME[num])
    return result if result else []

NUMBER_TO_NAME = {1: "One", 2: "Two", 3: "Three", 4: "Four", 
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

class TestByLength(unittest.TestCase):
    def test_single_digit_numbers(self):
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]), 
                         ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"])

    def test_empty_array(self):
        self.assertEqual(by_length([]), [])

    def test_with_strange_numbers(self):
        self.assertEqual(by_length([1, -1, 55]), ["One"])

if __name__ == '__main__':
    unittest.main()
```

In this script:
- The `NUMBER_TO_NAME` dictionary is defined to map digits to their names.
- The `by_length` function takes an array of integers, sorts the digits between 1 and 9, reverse the sorted array, and then converts each digit to its name.
- The `unittest` module is used to define test cases for the `by_length` function. 

The `test_single_digit_numbers`, `test_empty_array`, and `test_with_strange_numbers` test cases cover different scenarios mentioned in the problem statement.

When you run this script, the `unittest` framework executes each test case and reports any differences between the expected outcome and the actual outcome. 

This approach allows you to confidently validate your function's behavior and ensure it handles various scenarios correctly.