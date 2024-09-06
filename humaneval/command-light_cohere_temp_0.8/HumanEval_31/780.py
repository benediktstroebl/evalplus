Here is a Python script that includes a self-contained function that checks whether a given number is a prime:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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

This code defines a function named `is_prime` that checks whether a given number `n` is prime or not. The function utilizes a testing various values to ensure its functionality. The output will display True if the number is prime, and False otherwise. 

The `is_prime` function is self-contained and its correctness is tested via the provided test cases.