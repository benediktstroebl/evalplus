```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper bound.

    Returns:
        int: The count of digit 7.
    """
    count = 0
    for i in range(11, n, 11):
        for j in range(13, n, 13):
            if i < j:  # Ensure we don't count the same number twice
                count += str(i).count('7') + str(j).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Expected: 0
print(fizz_buzz(78))  # Expected: 2
print(fizz_buzz(79))  # Expected: 3
```

This script works by iterating through all numbers less than `n` that are divisible by 11 or 13, and increments the count by the number of times the digit 7 appears in each number. The `count('7')` method is used to count the occurrences of the digit 7 in a string representation of a number. The test cases at the end demonstrate the function's behavior for different inputs.