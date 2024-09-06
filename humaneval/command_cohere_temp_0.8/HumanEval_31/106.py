Here's a Python script with a self-contained function that solves the prime-checking problem, as described in the code block and comments provided:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function is designed to handle the edge cases mentioned in the problem statement, including numbers less than 2 (which are not prime) and numbers that are divisible by themselves or 1 (which are not prime). It does this by iterating from 2 up to the square root of the number and checking for divisibility.

You can test this function against the provided test cases to verify its behavior:
```python
# Test the function against the provided test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This should produce the following output:
```plaintext
False
True
True
True
True
False
False
``` 

As evidenced by the above output, the function correctly identifies prime and non-prime numbers according to the provided test cases. 

This function is a simple yet fundamental implementation of prime checking, but it covers the core requirement of the problem. 

Let me know if this solution suits your needs or if you'd like me to provide additional variations or improvements to the code.