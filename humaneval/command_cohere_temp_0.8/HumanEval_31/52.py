```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement and satisfies the provided test cases. It checks if a number is less than 2, it returns false. Then, it iterates from 2 up to the square root of the number and checks if the number is divisible by any of these integers. If it is, it returns false. If it isn't, it returns true.  This fundamental approach ensures prime number determination.