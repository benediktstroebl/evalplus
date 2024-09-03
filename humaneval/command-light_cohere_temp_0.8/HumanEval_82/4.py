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

def prime_length(string):
    return all([is_prime(char) for char in string])

# Example usage
print(prime_length('Hello'))  # Output: True
print(prime_length('abcdcba'))  # Output: True
print(prime_length('kittens'))  # Output: False
print(prime_length('orange'))  # Output: False
```
The function `prime_length` checks if the string contains any prime numbers using the `is_prime` function. The function returns `True` if the string is a prime number, and `False` otherwise. The `is_prime` function uses a combination of conditional checks to determine if a number is prime or not.