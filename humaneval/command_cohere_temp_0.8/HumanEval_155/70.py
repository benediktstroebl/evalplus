Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
        count_ev = 0
        count_od = 0
        str_num = str(num)
        for char in str_num: 
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_ev += 1
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_od += 1
        return (count_ev, count_od)
    else:
        return "Incorrect argument type"
```

And here is a test suite that checks if the function behaves as intended:
```python
import unittest

class TestEvenOddCount(unittest.TestCase):
    def test_even_odd_count_true(self):
        self.assertEqual(even_odd_count(123), (1, 2))
        self.assertEqual(even_odd_count(4567), (2, 1))
        self.assertEqual(even_odd_count(10), (2, 0))

    def test_even_odd_count_negative(self):
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_even_odd_count_zero(self):
        self.assertEqual(even_odd_count(0), (2, 0))

    def test_even_odd_count_non_int(self):
        result = even_odd_count("string")
        self.assertEqual(result, "Incorrect argument type")

if __name__ == '__main__':
    unittest.main()
```

In the test suite, the test_even_odd_count_true method tests the function on various valid inputs to check if the function computes the correct even and odd digit counts. The test_even_odd_count_negative and test_even_odd_count_zero methods test the function's behavior with negative and zero inputs, respectively. Finally, the test_even_odd_count_non_int method verifies that the function produces an error when given a non-integer input. 

When the script is run, the unittest.main() call executes the test suite. Upon passing, the tests confirm the function's correctness, producing the expected behavior.