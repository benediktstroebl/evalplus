```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one of the numbers must be non-zero")
    return max(set(divisor(a) for divisor in divisors(b)))

def divisors(n):
    yield [1,  n] + [n // d for d in range(1, n // 2 + 1)]

test_ GreatestCommonDivisor.py:
import unittest

class TestGreatestCommonDivisor(unittest.TestCase.TestCase):
    def test_gcd(self):
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5

if __name__ == '__main__':
    unittest.main()
```