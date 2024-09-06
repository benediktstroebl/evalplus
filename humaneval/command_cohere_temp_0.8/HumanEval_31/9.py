```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. It checks if `n` is less than 2, which would make it not prime, and if `n` is divisible by any number from 2 to the square root of `n`, which would also make it not prime. If neither of these conditions are met, then `n` is prime, and the function returns `True`. 

This code assumes that the tests include checking if the function behaves correctly for small prime and non-prime numbers, as well as edge cases such as `n < 2` and `n == 1`. Adding these tests would indeed verify the correctness of this solution.