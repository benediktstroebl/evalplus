Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a number is prime or not. It first checks if the number is less than 2, returning `False` if so. It then iterates from 2 up to the square root of the number, checking whether the number is divisible by any of these integers, and if so, it returns `False`. If we reach the end of the loop, the number is not divisible by any integer within this range, and it is therefore prime, so the function returns True.

This algorithm is relatively efficient because it only needs to iterate up to the square root of the number. For larger numbers, this algorithm is significantly faster than a brute-force check that iterates up to the number itself.