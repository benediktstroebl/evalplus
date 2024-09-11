```python
def count_sevens(n: int):
    """
    Helper function to count the number of times the digit 7 appears in a given number.

    Args:
        num (int): The number to count the digit 7 in.

    Returns:
        int: The number of times the digit 7 appears in num.
    """
    return str(num).count('7')


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit for the integers to check.

    Returns:
        int: The number of times the digit 7 appears in the integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_sevens(i)
    return count


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Expected output: 0
    print(fizz_buzz(78))  # Expected output: 2
    print(fizz_buzz(79))  # Expected output: 3
```

This script defines two helper functions: `count_sevens` which counts the number of times the digit 7 appears in a given number, and `fizz_buzz` which calculates the total count of digit 7 in integers less than `n` which are divisible by 11 or 13.