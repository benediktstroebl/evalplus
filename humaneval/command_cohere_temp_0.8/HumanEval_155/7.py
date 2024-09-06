Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_ev = 0
    count_od = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_ev += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_od += 1
    return (count_ev, count_od)
```

And here is a test suite to ensure that the function behaves as expected:
```python
# Test suite
import unittest

class TestEvenOddCount(unittest.TestCase):
    def test_even_odd_count_1(self):
        self.assertEqual(even_odd_count(123), (1, 2))
    def test_even_odd_count_2(self):
        self.assertEqual(even_odd_count(-12), (1, 1))
    def test_even_odd_count_3(self):
        self.assertEqual(even_odd_count(0), (0, 0))
    def test_even_odd_count_4(self):
        self.assertEqual(even_odd_count(195), (2, 1))
    def test_even_odd_count_5(self):
        self.assertEqual(even_odd_count(687), (3, 2))

if __name__ == '__main__':
    unittest.main()
```

This way, the even_odd_count function can be called with different test inputs to check if it returns the expected results.