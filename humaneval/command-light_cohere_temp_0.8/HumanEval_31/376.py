```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This function, `is_prime`, uses a basic algorithm to determine if a given number is prime or not. It iterates up approach the both the 2 and 3 tests and then uses a simple loop to check divisibility up to the square root of the number. 

It's a good starting point for most cases and can be easily modified or improved for better efficiency or more robust prime checking.