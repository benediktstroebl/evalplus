```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError("Input number must be positive")

    return number - int(number)


# Test cases
import unittest

class TestTruncateNumberFunction(unittest.TestCase):

    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(10.99), 0.99)
        self.assertAlmostEqual(truncate_number(5.0), 0.0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-3.5)

if __name__ == '__main__':
    unittest.main()
```