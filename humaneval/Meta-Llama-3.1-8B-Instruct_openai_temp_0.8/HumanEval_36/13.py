### Fizz Buzz with Digit 7 Count
#### Problem Description
This script counts the number of times the digit 7 appears in integers less than a given number `n` that are divisible by 11 or 13.

#### Solution
```python
def count_digit(n: int, digit: int) -> int:
    """
    Count the occurrences of a digit in a range of numbers.
    
    Args:
    n (int): The end of the range (exclusive).
    digit (int): The digit to count.
    
    Returns:
    int: The number of times the digit appears.
    """
    count = 0
    for i in range(1, n):
        # Convert the number to a string to easily count the digit
        if str(digit) in str(i):
            count += 1
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit of the range.
    
    Returns:
    int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Count the occurrences of the digit 7
            count += count_digit(i, 7)
    return count


# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines two functions: `count_digit` and `fizz_buzz`. The `count_digit` function counts the occurrences of a given digit in a range of numbers, and the `fizz_buzz` function uses this function to count the occurrences of the digit 7 in integers less than a given number `n` that are divisible by 11 or 13.