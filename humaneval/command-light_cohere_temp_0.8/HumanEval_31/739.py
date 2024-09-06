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

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This function, named `is_prime()`, accepts an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. 

The function uses several logical tests to determine if a number is prime. The function first checks if `n` is less than or equal to one, and if so, it returns `False` since prime numbers must be greater than 1. 

The function then checks if `n` is of the form divisible by 2 or 3, and if so, it returns `False` since these are not prime numbers. 

The function then initializes a variable `i` to 5 and sets up a while loop that continues until `i * i` exceeds the given number. The function then checks if `n` is divisible by the current value of `i` or the value of `i` plus 2, and if so, it returns `False` since these are not prime numbers. 

Finally, if none of the above conditions are met, the function returns `True`, indicating that the number is a prime number.