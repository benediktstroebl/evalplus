Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp_num = abs(num)
    while temp_num != 0:
        digit = temp_num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        temp_num //= 10
    return (count_even, count_odd)
```
This function initially handles the edge case where num is 0, returning a result of (0, 0). It then proceeds to count the number of even and odd digits in the absolute value of num. The use of a while loop enables iteration through the digits, and the modulus operator helps determine the remainder of each digit, which is then used to identify whether it is even or odd. 

To demonstrate the functionality of the even_odd_count function, we can import the Python unittest module and create a few test cases. Here's how you can do that:
```python
import unittest

def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    temp_num = abs(num)
    while temp_num != 0:
        digit = temp_num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        temp_num //= 10
    return (count_even, count_odd)

class TestEvenOddCount(unittest.TestCase):
    def test_even_odd_count_with_negative_int(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_even_odd_count_with_positive_int(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_even_odd_count_with_zero(self):
        self.assertEqual(even_odd_count(0), (0, 0))

if __name__ == '__main__':
    unittest.main()
```
This script will automatically run the test cases defined in the TestEvenOddCount class when executed directly. Each test case asserts that the result of calling even_odd_count matches the expected tuple of (count_even, count_odd). 

You can add more test cases to cover a broader range of integer inputs to ensure the correctness of the even_odd_count function.