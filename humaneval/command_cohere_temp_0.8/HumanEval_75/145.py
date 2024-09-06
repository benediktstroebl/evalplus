```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a > 1:
        prime_factors = []
        for i in range(2, int(a ** 0.5) + 1):
            while a % i == 0:
                prime_factors.append(i)
                a //= i
            if a == 1:
                break
        if len(prime_factors) == 3:
            return True
    return False
```

This Python script defines a function called `is_multiply_prime(a)` that checks whether a given number `a` is the product of three prime numbers. It works by first assuming that `a` is greater than 1 and less than 100, which is the given constraint in the prompt. It then iterates through factors from 2 up to the square root of `a`, and repeatedly divides `a` by the current factor until it is no longer divisible. The found prime factors are collected in the `prime_factors` list. If the length of this list is 3, indicating that three prime factors were found, the function returns `True`, indicating that the number is the product of three prime numbers. Otherwise, it returns `False`.