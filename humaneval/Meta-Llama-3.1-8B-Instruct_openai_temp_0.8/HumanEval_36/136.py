```python
def count_digit_7(n: int) -> int:
    """
    Count the occurrences of digit 7 in the range of numbers from 0 to n-1.
    
    Args:
        n (int): Upper limit of the range (exclusive).

    Returns:
        int: The number of times the digit 7 appears in the given range.
    """
    count = 0
    for i in range(n):
        # Convert the number to a string to check each digit individually
        for digit in str(i):
            # Check if the current digit is '7'
            if digit == '7':
                count += 1
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit of the range (exclusive).

    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(n):
        # Check if the current number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit_7(i + 1)
    return count


# Example usage:
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```