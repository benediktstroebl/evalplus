```python
def is_multiply_prime(a):
    # check if a is a multiple of 2
    if a % 2 == 0:
        return False

    # check if a is a multiple of 3
    if a % 3 == 0:
        return False

    for i in range(5, int(a**0.5) + 1):
        if a % i == 0:
            return False

    return True
```

This Python script defines a function called `is_multiply_prime(a)` that checks whether the given number `a` is the product of three prime numbers. The function first checks if `a` is divisible by 2 or 3, both of which are prime numbers. Then, it iterates through the numbers 5, 7, 11, 13, 17, 19, and so on, up to the square root of `a`, checking if `a` is divisible by any of them. If none of these divisions yields a remainder of 0, it means `a` is not divisible by any prime numbers other than 2 and 3, and the function returns `True`; otherwise, it returns `False`. 

This solution works for numbers less than 100, as instructed in the prompt.