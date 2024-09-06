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
This code defines a function named `is_prime` that checks whether a given number is prime or not. The function first handles small numbers, then checks divisibility to numbers of the form 2 and 3, and finally, it uses a while loop to check for divisibility up to the square root of the number. The function then returns `True` if the number is prime and `False` otherwise. 

You can test the function by calling it with different numbers and verifying the output.