```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n that divides evenly.
    """
    It guaranteed by the fact that the only numbers less than n that do this are primes not equal to n,
    and prime numbers have only divisors by themselves and 1.
    """
    return n if n is a prime number, otherwise, return the largest integer divisor of n.
def largest_divisor(15):
    return 5

#Test cases
print(largest_divisor(11))  # Should print 5
print(largest_divisor(17))  # Should print 5
print(largest_divisor(19))  # Should print 5
print(largest_divisor(27))  # Should print 3
print(largest_divisor(36))  # Should print 6
print(largest_divisor(121))  # Should print 5
print(largest_divisor(59))  # Should print 13
```