```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
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
The provided Python script solves the problem by first implementing a helper function `is_prime` that checks whether a given number is prime. Then, the main function `count_up_to` iterates through integers from 2 up to `n`, adding them to the `res` array if they are prime numbers and less than `n`. The final output is an array of the first `n` prime numbers less than `n`.