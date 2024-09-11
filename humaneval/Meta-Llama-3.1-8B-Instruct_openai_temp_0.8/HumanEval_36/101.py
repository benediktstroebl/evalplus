```python
def count_digit_7(num: int) -> int:
    """
    Count the number of times the digit 7 appears in the number.
    
    Args:
    num: The number to count the digit 7 in.
    
    Returns:
    The number of times the digit 7 appears in the number.
    """
    return str(num).count('7')


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n: The upper bound.
    
    Returns:
    The number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit_7(i)
    return count


# Example usage
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

This script defines two functions: `count_digit_7` counts the occurrences of the digit 7 in a given number, and `fizz_buzz` counts the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The example usage demonstrates the function's behavior with the given test cases.