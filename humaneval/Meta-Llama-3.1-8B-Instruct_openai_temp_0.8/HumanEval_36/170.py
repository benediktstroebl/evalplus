```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit '7'
            str_i = str(i)
            # Count the occurrences of '7' in the string
            count += str_i.count('7')
    return count

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

However, since we are converting each number to a string for counting '7', this approach is inefficient for large inputs. A more efficient way to solve this problem would be to use integer arithmetic to directly count the occurrences of '7' in each number:

```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Count the occurrences of '7' in the number by iteratively dividing by 10 and checking the last digit
            while i > 0:
                count += i % 10 == 7
                i //= 10
    return count

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```