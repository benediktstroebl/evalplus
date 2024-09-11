```python
def count_digit_7(n: int) -> int:
    """
    Count the number of times the digit 7 appears in the given number.
    
    Args:
    n (int): The number to count the digit 7 from.

    Returns:
    int: The number of times the digit 7 appears in the given number.
    """
    count = 0
    for digit in str(n):
        if digit == '7':
            count += 1
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit for the integers to check.

    Returns:
    int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit_7(i)
    return count


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Expected output: 0
    print(fizz_buzz(78))  # Expected output: 2
    print(fizz_buzz(79))  # Expected output: 3
```

This script defines two functions: `count_digit_7` and `fizz_buzz`. The `count_digit_7` function counts the number of times the digit 7 appears in a given number. The `fizz_buzz` function uses `count_digit_7` to count the number of times the digit 7 appears in integers less than the given number `n` which are divisible by 11 or 13.