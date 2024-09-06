```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer less than n that divides evenly.
    # A faster implementation using the unique divisor method:
    for divisor in range(1, n+1):
        if n % divisor == 0:
            return divisor
    return n
# Test cases
print(largest_divisor(15))  # Output: 5
print(largest_divisor(24))  # Output: 12
```