```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in the specified range of numbers.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script works by iterating over all integers less than `n`, checking if each integer is divisible by 11 or 13, and counting the number of times the digit 7 appears in the string representation of each integer. The final count is returned as the result of the `fizz_buzz` function.