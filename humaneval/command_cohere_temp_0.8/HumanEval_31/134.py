```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function iterates from 2 up to `n - 1` to determine if the number is prime. It returns `False` if the number is less than 2 or if it divides evenly against any number in that range. It returns `True` otherwise, indicating that the number is prime. This approach is efficient and suits the problem requirements. 
The `range(2, n)` is used to loop through the numbers from 2 to `n - 1` inclusive. This is done because we only need to test divisors up to `n - 1` to determine if `n` is prime. Testing divisors larger than `n - 1` would result in overflow and inaccurate prime checks. 
The tests provided evaluate the function's correctness against known prime and non-prime numbers. Failing to include these tests would render the response incomplete and potentially misleading for others trying to solve this problem.