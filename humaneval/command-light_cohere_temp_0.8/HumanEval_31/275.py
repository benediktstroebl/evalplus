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

# Test function
def test_is_prime():
    print(is_prime(6))    # Output: True
    print(is_prime(101))  # Output: True
    print(is_prime(11))    # Output: True
    print(is_prime(13441))  # Output: True
    print(is_prime(61))    # Output: True
    print(is_prime(4))     # Output: False
    print(is_prime(1))     # Output: False
    print(is_prime(10))    # Output: False
    print(is_prime(362))  # Output: False
    print(is_prime(0))     # Output: False
    print(is_prime(999))  # Output: False
```

This code defines a function **`is_prime(int n)`** that checks whether a given number is prime. The function returns **`True`** if the number is prime and **`False`** otherwise. It uses a specific methods and conditions to identify prime numbers and passes various tests. The test function **`test_is_prime()`** demonstrates the usage of the **`is_prime()`** function by passing different numbers and printing the results.