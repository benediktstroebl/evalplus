```python
def count_sevens(n: int):
    """
    Count the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for the range of numbers to check.

    Returns:
    int: The number of times the digit 7 appears in the specified numbers.
    """
    return sum(
        str(num).count('7') 
        for num in range(n) 
        if num % 11 == 0 or num % 13 == 0
    )


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for the range of numbers to check.

    Returns:
    int: The number of times the digit 7 appears in the specified numbers.
    """
    return count_sevens(n)


# Example usage
print(fizz_buzz(50))   # Output: 0
print(fizz_buzz(78))   # Output: 2
print(fizz_buzz(79))   # Output: 3
```

This script defines two functions: `count_sevens` and `fizz_buzz`. `count_sevens` is a helper function that counts the occurrences of the digit 7 in the specified range of numbers. It uses a generator expression to iterate over the numbers in the range, check if they are divisible by 11 or 13, and count the occurrences of '7' in their string representation. The `fizz_buzz` function simply calls `count_sevens` with the given argument. The example usage demonstrates the function's behavior with the provided test cases.