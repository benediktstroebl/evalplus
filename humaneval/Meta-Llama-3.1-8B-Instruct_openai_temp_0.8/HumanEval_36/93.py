```python
def count_sevens(n: int) -> int:
    """
    Count the occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive) for the range of numbers to check.

    Returns:
    int: The number of times the digit 7 appears in the specified numbers.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to check for the digit 7
            str_i = str(i)
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (inclusive) for the range of numbers to check.

    Returns:
    int: The number of times the digit 7 appears in the specified numbers.
    """
    return count_sevens(n)


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Expected output: 0
    print(fizz_buzz(78))  # Expected output: 2
    print(fizz_buzz(79))  # Expected output: 3
```

In this script, the `count_sevens` function counts the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13, while the `fizz_buzz` function is an alias for `count_sevens` with the same functionality. The test cases are included at the end of the script to demonstrate its correctness.