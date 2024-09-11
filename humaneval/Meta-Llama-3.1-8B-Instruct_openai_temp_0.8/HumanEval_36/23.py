```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit for the integers to check.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This Python script defines a function `fizz_buzz(n)` that counts the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13. The function iterates over the range from 1 to `n-1`, checks for divisibility by 11 or 13, converts the integer to a string, counts the occurrences of '7', and accumulates the counts. The function returns the total count.