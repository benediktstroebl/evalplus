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

# Test suite
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This function, `is_prime()`, accepts an integer `n` as input and outputs a boolean indicating whether `n` is a prime number or not. 

The function uses a series of conditions and checks to determine if `n` is prime or not. 

These conditions include: 
1. If `n` is less than or equal to 1, it returns `False`. 
2. If `n` is less than or equal to 3, it returns `True`. 
3. If `n` is of the form 2 or 3, it returns `False`. 
4. The function starts with `i` equal to 5 and iterates until the square of `i` is less than or equal to `n`. 

5. If `n` is divisible by any number in this range or the square of `n` is divisible by `i` or `i + 2`, it returns `False`. 
6. If the loop completes without any such of these conditions, it returns `True`, indicating that `n` is a prime number.