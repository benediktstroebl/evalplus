```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive) for the range of numbers to check.

    Returns:
        int: The count of numbers less than n which are divisible by 11 or 13 and contain the digit 7.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a function `fizz_buzz(n)` that checks all integers less than `n`, counting those that are divisible by 11 or 13 and contain the digit 7. The function then returns this count. The test cases are included at the end to demonstrate the function's behavior.