Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
        count_even = 0
        count_odd = 0
        str_num = str(num)
        for char in str_num: 
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_even += 1
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_odd += 1
        return (count_even, count_odd)
    else:
        raise TypeError("Input must be an integer")
```

And here is a test suite that verifies the functionality of the function:
```python
import unittest

class TestEvenOddCount(unittest.TestCase):
    def test_even_odd_count_negative_input(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_even_odd_count_positive_input(self):
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_even_odd_count_zero(self):
        self.assertEqual(even_odd_count(0), (0, 0))

    def test_even_odd_count_mixed_input(self):
        self.assertEqual(even_odd_count(421), (2, 1))

    def test_even_odd_count_string_input(self):
        with self.assertRaises(TypeError):
            even_odd_count("123")

    def test_even_odd_count_non_integer(self):
        with self.assertRaises(TypeError):
            even_odd_count(None)

if __name__ == '__main__':
    unittest.main()
```

This test suite contains six different tests that cover different scenarios which should hopefully catch any potential bugs or edge cases. 

Note that the current solution assumes that the input is a valid integer with a single decimal point. If the input number could be different in any way (e.g., a longer decimal number, different kind of integer, etc.), the code might need to be adjusted accordingly.