```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # Largest divisor found, now checking if there's a larger one
            if j > i:  # There is, because of the division behavior for larger divisors
                return j
            else:
                return i
    else:
        return 1  # If no divisor is found, return 1

# Testing the function
def test_largest_divisor():
    assert largest_divisor(15) == 5
    assert largest_divisor(18) == 6
    assert largest_divisor(25) == 5
    assert largest_divisor(36) == 9
    assert largest_divisor(52) == 13
    assert largest_divisor(60) == 20
    assert largest_divisor(1) == 1
    assert largest_divisor(100) == 100

test_largest_divisor()
```