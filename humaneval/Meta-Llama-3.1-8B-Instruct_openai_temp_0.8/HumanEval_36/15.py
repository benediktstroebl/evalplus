```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz(n)` that iterates over the range of numbers from 0 to `n-1`. For each number, it checks if it is divisible by either 11 or 13. If it is, it converts the number to a string and counts the occurrences of the digit '7'. The total count is then returned.

The test cases at the end demonstrate the function's behavior for different inputs.