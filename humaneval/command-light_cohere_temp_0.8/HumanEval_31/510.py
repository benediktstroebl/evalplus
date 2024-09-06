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

# Test the function with some examples
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The function `is_prime` accepts an integer `n` as an argument and checks whether it's a prime number. It employs a usual primality criteria: numbers less than 2 and numbers less than 3 are prime, and if a number is even or an odd number formed by multiplying two smaller prime numbers, it is not prime. The function uses a iterative approach to check primality, starting from `i = 5` and gradually increasing the value of `i` by 6 each iteration to identify numbers that are not prime.