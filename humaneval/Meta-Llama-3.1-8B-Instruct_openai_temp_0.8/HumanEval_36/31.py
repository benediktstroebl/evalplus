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
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to string to easily check for digit 7
            str_i = str(i)
            # Count the occurrences of digit 7
            count += str_i.count('7')
    return count

# Test the function
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script uses a simple loop to iterate over all integers less than the input `n`. For each number, it checks if it's divisible by 11 or 13. If it is, it converts the number to a string and uses the `count` method to count the occurrences of the digit 7. The total count is then returned.