```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    """
    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(20))  # Expected output: 20
```

This script defines a function `largest_divisor` that finds the largest divisor of a given number `n` by checking all numbers smaller than `n` in descending order. As soon as it finds a divisor, it returns it. The script also includes some test cases to demonstrate the function's behavior.