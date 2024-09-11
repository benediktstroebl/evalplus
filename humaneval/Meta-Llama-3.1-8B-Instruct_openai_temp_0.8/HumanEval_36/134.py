```python
def count_sevens(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper bound for the numbers to check.

    Returns:
        int: The count of 7s in the numbers.
    """
    count = 0  # Initialize count to 0
    for i in range(1, n):  # Loop through numbers 1 to n-1
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            count += str(i).count('7')  # Increment count by the number of 7s in the number
    return count  # Return the total count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_sevens(n)  # Call count_sevens to get the count


# Test the function
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```

In this script, the `count_sevens` function is used to count the occurrences of the digit 7 in numbers that are multiples of 11 or 13. This function is then used by the `fizz_buzz` function to perform the specified task. The `fizz_buzz` function is tested with the provided example inputs to demonstrate its correctness.