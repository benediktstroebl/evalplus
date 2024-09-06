```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. It then iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in this range. If the number is divisible by any of these, it returns `False`. If it is not, it returns `True`. This algorithm is quite efficient, as the worst-case time complexity is O(sqrt(n)), and the average time complexity is O(ln(n)). This is because the loop only runs up to the square root of the number at most, and the number of iterations is typically less than the logarithm of the number.

This function is more sophisticated than the provided `is_prime` function, which only checks divisibility by integers 1, 2, and 3, and may not produce the correct result for some test cases.