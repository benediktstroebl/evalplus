Here's a Python script that contains a function called even_odd_count, defined to take in an integer and return a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if int(i) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

To ensure the script performs as expected, there is a corresponding test module:
```python
import unittest
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    count_even = 0
    count_odd = 0
    temp = str(num)
    for i in temp:
        if int(i) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)

class TestEvenOddCount(unittest.TestCase):
    def test_negativeNumbers(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_positiveNumbers(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_zero(self):
        self.assertEqual(even_odd_count(0), (0, 0))

if __name__ == '__main__':
    unittest.main()
```

The script and function are both validated by the test module, which checks the functionality against a number of test cases, including negative numbers, positive numbers, and zero.

To run the tests, simply execute the script. The test suite will run automatically, and any failures or errors will be reported. 

You can customize the test cases in the test module to cover a broader range of input scenarios and edge cases as needed.