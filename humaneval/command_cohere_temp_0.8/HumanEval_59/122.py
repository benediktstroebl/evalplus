```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Bubble up digits from the least significant position (rightmost)
    # As soon as a digit is not a prime, stop bubbling and return the largest prime
    # encountered so far
    largest_prime = n
    for digit in reversed(str(n)):
        if digit != '1' and all(map(lambda x: x % digit != 0, range(2, int(digit**0.5) + 1)) and digit != 1:
            largest_prime //= digit
    return largest_prime
```