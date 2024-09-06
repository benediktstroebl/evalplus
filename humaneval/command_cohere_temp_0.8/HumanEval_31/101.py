Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement and test scenarios provided, including cases of prime and non-prime numbers. 
The `range()` function is used for loop optimization, and brute-force exponentiation is avoided through the use of `int(n**0.5)`. 

This approach provides efficient prime-checking for the given input range. 
The provided tests correspond to the given scenarios and accurately evaluate the function's performance. 
This code promotes readability and maintains Python's style guidelines. 

It's important to ensure that any modifications to this function still align with the given tests to ensure accurate prime-checking functionality.