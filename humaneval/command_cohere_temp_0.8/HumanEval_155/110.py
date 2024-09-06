Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int):
        num_str = str(num)
        count_even = 0
        count_odd = 0
        for char in num_str:
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_even += 1
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_odd += 1
        return (count_even, count_odd)
    else:
        raise TypeError("Input num must be an integer")
```

And here is a test suite that can be used to verify the functionality of the solution:
```python
import unittest
def test_even_odd_count():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(15) == (1, 1)
    assert even_odd_count(898) == (2, 2)

class TestEvenOddCount(unittest.TestCase):
    def test_even_odd_count(self):
        test_even_odd_count()

if __name__ == '__main__':
    unittest.main()
```

The test suite contains a test function that tests the even_odd_count function with a variety of inputs to verify its correctness. And the TestCase class allows us to organize and run the tests as part of a broader test suite. 

To execute the test suite run the following command in your terminal:
```bash
python -m unittest test_even_odd_count.py
``` 

This will execute the test suite and provide you with a detailed report on the tests that failed, passed, or raised errors.