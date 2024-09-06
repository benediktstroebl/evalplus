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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This Python code defines a function `is_prime` that checks whether a given number `n` is a prime number. The function uses an combination of conditions and algorithms to determine primality, including checking divisibility by 2 and 3, and then using a `while` loop to continue checking larger prime factors until the square of the number exceeds the square of the loop variable `i`.  The test cases are provided to verify the correctness of the `is_prime` function, and the expected outputs are printed.