Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in that range. If the number is divisible by any of them, it returns `False`. However, if it isn't, it returns `True`, indicating that the number is prime. 

This function is crafted to be efficient for its purpose, as the range of the loop starts from 2, which is the smallest prime number. This is because prime numbers greater than 2 will all be even, and so they will all be divisible by 2. Thus, the range can be limited to integers only between 2 and the square root of the given number, as any divisors present must be equal to either 1 or the square root itself. 

This is reflected in the test suite, which consists of a variety of numbers that can be categorized as either prime or non-prime. 

To tackle potential edge cases, the function also handles numbers less than 2, returning `False` for any input value that falls into that category.