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
The function is_prime takes an integer n as input and returns true if n is a prime number, and false otherwise. The function first checks if n is less than or equal to 1 and returns false. Then, it checks if n is of the form 2 or 3, and returns false since those numbers are not prime. The function then starts a prime factorization by assigning the value 5 to i and checks if n is divisible by i or i + 2. If n is divisible, the function returns false. Otherwise, it returns true.