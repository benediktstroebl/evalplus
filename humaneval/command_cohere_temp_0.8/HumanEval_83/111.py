```python
def starts_one_ends(n):
    pos_num = str(n)
    if pos_num.isdigit():
        num_list = [int(val) for val in pos_num]
        if num_list[0] == 1 or num_list[-1] == 1:
            return 2
        else:
            return 1
    else:
        return 0
```
This function determines the count of numbers that start or end with 1, then subsequently checks if the passed integer is a digit string, initializing an empty list to store individual digits, subsequently converting the passed integer to a list of integers. If the first or last integer is 1, then the count equals 2, otherwise, it is reset to 1. Thus, the function accordingly returns the updated count. 

The following tests evaluate this function:
```python
test_cases = [
    (1, 1),
    (10, 2),
    (11, 2),
    (111, 3),
    (1231, 3),
    (98765, 4),
]
```

Moreover, here is the code to execute the tests:
```python
import unittest

class TestStartEndOne(unittest.TestCase):
    def test_start_end_one(self):
        for n, expected in test_cases:
            with self.subTest(n=n):
                result = starts_one_ends(n)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
```

This test suite contains a list of test cases to verify the correctness of the `starts_one_ends` function. The function is tested against a variety of arguments, and the expected result is compared with the actual result, and the test passes if they are equal. If not, it prints an error message, highlighting the specific scenario where the function does not deliver the expected result.  In the main function, the `unittest.main()` method executes the test suite when this script is run directly. 

Lastly, to execute the tests, type the following command into your terminal:
```
python TEST.py
``` 

This will proceed to run the tests, and subsequent test results will be displayed in your terminal.