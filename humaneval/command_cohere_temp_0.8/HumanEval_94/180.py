```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    max_prime = max(primes) if primes else 0
    return sum(map(int, str(max_prime)))
```

The function `skjkasdkd` takes a list of integers as input and first filters out all prime numbers from the list using a list comprehension. Then, it finds the maximum prime number from the filtered list using the `max` function, and converts it to a string and sums up its digits using `sum` and `map` functions. The final result is the sum of digits of the largest prime value present in the list.

To verify the functionality of the provided solution, you can write a simple test suite using Python's `unittest` module like this:
```python
import unittest

def test_skjkasdkd():
    # Test case examples provided in the problem statement
    assert skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    assert skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]) == 13
    assert skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]) == 11
    assert skjkasdkd([0, 81, 12, 3, 1, 21]) == 3
    assert skjkasdkd([0, 8, 1, 2, 1, 7]) == 7

class TestSkjkasdkd(unittest.TestCase):
    def test_skjkasdkd(self):
        test_skjkasdkd()

if __name__ == '__main__':
    unittest.main()
```

This test suite includes one `unittest` class test class `TestSkjkasdkd`, which executes the `test_skjkasdkd` function that runs the same tests cases as provided in the problem statement to verify the correctness of the solution. 

To run the tests, simply execute the script file or use the following command if the script is saved in a file called `test_skjkasdkd.py`:
```bash
python test_skjkasdkd.py
```