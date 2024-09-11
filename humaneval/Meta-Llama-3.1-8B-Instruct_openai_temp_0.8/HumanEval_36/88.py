```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(11, n, 11):
        for digit in str(i):
            if digit == '7':
                count += 1
    for i in range(13, n, 13):
        for digit in str(i):
            if digit == '7':
                count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines the `fizz_buzz` function that iterates over all integers less than `n` which are divisible by 11 or 13, converts each integer to a string, checks each digit, and increments the count whenever it encounters the digit '7'. The function finally returns the total count.