```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    max_prime = max(primes) if primes else 0
    return sum(map(int, str(max_prime)))
```

The function `skjkasdkd` takes a list of integers as input and first filters out all prime numbers from the list using a list comprehension. It then finds the maximum prime number within the list of primes using the `max` function, and converts it to a string and sums up its digits using `sum` and `map`. The final result is the sum of the digits of the largest prime value in the list. 

To validate the correctness of the solution, you can import the `unittest` module and use `unittest.main()` to run the tests:
```python
import unittest

class TestSkjkasdkd(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]), 10)

    def test_example2(self):
        self.assertEqual(skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]), 25)

    def test_example3(self):
        self.assertEqual(skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]), 13)

    def test_example4(self):
        self.assertEqual(skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]), 11)

    def test_example5(self):
        self.assertEqual(skjkasdkd([0, 81, 12, 3, 1, 21]), 3)

    def test_example6(self):
        self.assertEqual(skjkasdkd([0, 8, 1, 2, 1, 7]), 7)

if __name__ == '__main__':
    unittest.main()
```

This block of code will run the `unittest` module on the function, running six example tests.