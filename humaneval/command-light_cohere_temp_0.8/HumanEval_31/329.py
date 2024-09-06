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
This function, named `is_prime`, takes an integer `n` as an argument and returns `True` if `n` is a prime number and `False` otherwise. It utilizes a single pass to determine if a number is prime:
1. To check if `n` is less than or equal to `1`, it returns `False`.
2. To handle numbers `2` and `3`, it returns `True` since `2` and `3` are prime numbers.
3. If `n` is not `2` or `3` (prime numbers), it starts checking for divisibility by `2` and `3`. If `n` is divisible by `2` or `3`, it returns `False`.
4. If the above conditions are not met, it starts checking for divisibility by `i` where `i` is a prime number less than or equal to the square root of `n`. It checks for divisibility by `i` and `i + 2`, and if `n` is divisible by `i` or `i + 2`, it returns `False`.
5. If the loop completes without any condition, it means `n` is a prime number. 
The function achieves a complete solution to the given problem and passes all the corresponding tests.