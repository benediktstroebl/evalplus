```python
def count_digit(n, digit):
    """Return the number of times the digit appears in n."""
    return str(n).count(str(digit))


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit.

    Returns:
    int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit(i, 7)
    return count


# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines two functions: `count_digit` and `fizz_buzz`. The `count_digit` function counts the number of occurrences of a given digit in a number. The `fizz_buzz` function uses this helper function to count the occurrences of the digit 7 in numbers less than the input `n` that are divisible by 11 or 13. The example usage at the end demonstrates the function's behavior with the provided test cases.