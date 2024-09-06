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
The `count_up_to()` function iterates through numbers from 2 up to `n` and adds each prime number that is less than `n` to the `res` list. The `is_prime()` function is used as a helper to check if a number is prime. The `range()` function is used to iterate through numbers up to `n`.

Here is a sample output of the function:
```
count_up_to(5) => [2,3]
count_up_to(11) => [2,3,5,7]
count_up_to(20) => [2,3,5,7,11,13,17,19]
```

This list contains the first five prime numbers under 20, which matches the test case's specified output.