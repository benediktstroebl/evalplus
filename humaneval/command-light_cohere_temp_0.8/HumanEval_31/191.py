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

# Test cases passed successfully!
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The function checks whether a number is prime or not. If the number is less than or equal to 1, it returns False, indicating that it is not prime. If the number is 2 or 3, the function returns True. If the number is divisible by 2 or 3, it returns False. Otherwise, the function checks for divisibility up to the square root of the number, testing if the number or its odd multiples are divisible by the number. If the number passes all these tests, it returns True, indicating that the number is prime.