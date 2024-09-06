Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in that range. If the number is divisible by any of them, it returns `False`. However, if neither condition is met by the time the square root is reached, it returns `True`, indicating that the number is prime. 

This implementation provides an efficient algorithm for checking primality, and it handles edge cases such as passing in values less than 2, which should not return prime results. 

This code should help solve the problem and pass the tests provided, including handling the edge cases mentioned in the prompt. Let me know if you would like me to explain any part of the code in more detail!