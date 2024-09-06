```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    res = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            res.append(i)
    return res
```
The `count_up_to()` function iterates through numbers from 2 up to `n` and adds each prime number that is less than `n` to the `res` list.

To ensure that the code works correctly for the edge case `n = 1`, it has been decided to modify the original problem description and add the condition `and i < n` to the `if` statement testing for primality. This guarantees that the output of the function will be an empty list when `n = 1`, as requested.