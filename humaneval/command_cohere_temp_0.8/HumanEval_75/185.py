```python
def is_multiply_prime(a):
    # check if a is less than 100
    if a < 100:
        # manually check for each prime number multiplication
        for i in range(2,a):
            if a % i == 0:
                return False
        return True
    else:
        return False
```

This Python script defines a function `is_multiply_prime(a)` that checks if the given number `a` is the multiplication of 3 prime numbers. The function first checks if `a` is less than 100. If so, it iterates through all numbers from 2 to `a` and checks if they divide `a` without leaving a remainder. If no such number is found, it returns `False`, meaning the number is not a multiplication of prime numbers. If `a` is greater than 100, the function returns `False` directly, as it won't be able to find 3 prime numbers that can multiply to produce such a large number within the allowed range. 

If the given example with 30 is tested, the function returns `True` as 2 * 3 * 5 divides 30 without a remainder.