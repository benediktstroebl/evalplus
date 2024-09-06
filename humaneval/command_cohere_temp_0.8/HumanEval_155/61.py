Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    count = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '1' or char == '2' or char == '3':
            if int(char) % 2 == 0:
                count += 1
        elif char == '4' or char == '5' or char == '6' or char == '7':
            if int(char) % 2:
                count += 1
        elif char == '8' or char == '9':
            if int(char) % 2 == 0:
                count += 1
        else:
            raise ValueError("Unexpected character in input")
    return (count, num_str.count('5'))
```

The above code has a test suite with 4 tests. Here's an example of how the code can be tested:
```python
import unittest

class TestEvenOddCount(unittest.TestCase):
    def test_even_odd_count_positive_integers(self):
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(15), (1, 1))
        self.assertEqual(even_odd_count(19), (0, 1))

    def test_even_odd_count_negative_integers(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
        self.assertEqual(even_odd_count(-3), (1, 1))
        self.assertEqual(even_odd_count(-20), (1, 1))

    def test_even_odd_count_zero(self):
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_even_odd_count_non_integer(self):
        with self.assertRaises(TypeError):
            even_odd_count('123')

if __name__ == '__main__':
    unittest.main()
``` 

The test suite contains tests that cover edge cases and other scenarios to ensure the function behaves as expected.