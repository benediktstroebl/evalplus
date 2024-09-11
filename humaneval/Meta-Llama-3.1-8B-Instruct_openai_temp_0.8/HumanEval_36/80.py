### Fizz Buzz Counter
#### Problem Description
Count the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

#### Solution

```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for the integers to be checked.

    Returns:
    int: The count of digit 7 appearances.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily iterate over its digits
            str_i = str(i)
            # Count the occurrences of '7' in the string
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines the `fizz_buzz` function, which takes an integer `n` as input. It then iterates over all integers less than `n`, checking if each number is divisible by 11 or 13. For each such number, it converts the number to a string and counts the occurrences of the digit '7'. The total count is then returned. The script includes test cases to demonstrate the function's behavior.