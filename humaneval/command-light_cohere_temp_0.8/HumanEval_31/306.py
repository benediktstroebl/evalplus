```python
def is_prime(n):
    if n <= 1:
        return False
    for i := 2; i*i <= n; i += 1:
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This code defines a function called is_prime that checks whether a given number is prime or not. The function iterates from 2 up and checks if the square of the current number is less than or equal to the given number. The function then checks for divisibility by checking if any integer greater than or equal to the square root of the number, divided by it, equals the given number.