```python
def is_multiply_prime(a):
    primes = []
    for i in range(2, a):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes) == 3
```

This function checks if the number `a` is the product of three prime numbers by first collecting all the prime numbers from 2 to `a` and then checking if their number is exactly 3. 

### Here is a unittest for this function:
```python
import unittest

def is_multiply_prime(a):
    primes = []
    for i in range(2, a):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes) == 3

class TestIsMultiplyPrime(unittest.TestCase):
    def test_is_multiply_prime_true(self):
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(52))

    def test_is_multiply_prime_false(self):
        self.assertFalse(is_multiply_prime(6))
        self.assertFalse(is_multiply_prime(28))
        self.assertFalse(is_multiply_prime(49))
        self.assertFalse(is_multiply_prime(96))

if __name__ == '__main__':
    unittest.main()
```

In this unittest, we test the function on various cases: true multiples of three primes and some not, and verify that the function returns the expected results.