Here's a Python script with a self-contained function `is_prime` that follows the problem statement and passes the tests provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function iterates through numbers from 2 up to the square root of the input number `n`, checking for divisibility. If the number is divisible by any integer within this range, it's not prime, and the function returns `False`. If the number is not divisible by any integer within this range, it's prime, and the function returns `True`. 

The provided tests in the markdown code block are sufficient to verify the correctness of this solution.