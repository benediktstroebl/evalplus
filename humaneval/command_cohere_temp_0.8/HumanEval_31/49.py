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

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning false immediately if so. It then iterates from 2 up to the square root of the number `n`, checking if the number is divisible by any other number. If the number is divisible by any other number in this range, it returns false, if not, it returns true.

This solution corresponds to the test cases provided, and should solve the problem you have described. Feel free to ask any more questions or request further assistance!