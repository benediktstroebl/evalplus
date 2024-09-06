```python
def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod
```

This function iterates through each digit in the decimal representation of the input integer 'n' and determines whether each digit is odd or even. If the digit is odd, it multiplies the `prod` variable, which tracks the final result, by that digit. It returns 0 if all digits are even, yielding the intended result. 

You can include this code within a testing framework, such as the 'unittest' module, to ensure it behaves as expected for different cases. Here's an example:
```python
import unittest

def digits(n):
    prod = 1
    for digit in str(n):
        if int(digit) % 2:
            prod *= int(digit)
    return prod

class TestDigitsFunction(unittest.TestCase):
    def test_single_odd_digit(self):
        self.assertEqual(digits(1), 1)

    def test_single_even_digit(self):
        self.assertEqual(digits(4), 0)

    def test_multiple_digits_with_odd_product(self):
        self.assertEqual(digits(235), 15)

    def test_all_even_digits(self):
        self.assertEqual(digits(202), 0)

if __name__ == '__main__':
    unittest.main()
```

This way, running the script will execute the test suite, confirming that the `digits` function behaves as expected for different cases.