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
    for i in range(2, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit 7
            str_i = str(i)
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

In this script, the `fizz_buzz` function takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a simple loop to iterate over the range from 2 to `n-1` (since the problem statement excludes `n`), checks for divisibility by 11 or 13, and counts the occurrences of the digit 7 for each divisible number. The results are accumulated and returned at the end. The test cases demonstrate the function's correctness for the provided examples.