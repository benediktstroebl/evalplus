```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

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

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script uses two nested loops to iterate over the numbers less than `n` that are divisible by 11 or 13. It converts each number to a string and checks each digit. If the digit is 7, it increments the count. The function then returns the total count.