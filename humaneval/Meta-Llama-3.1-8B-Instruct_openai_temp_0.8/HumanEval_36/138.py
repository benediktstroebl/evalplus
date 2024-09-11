```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
        n (int): The upper limit for the range of numbers to check.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count


# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz(n)` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a loop to iterate over the range of numbers from 1 to `n-1`, checks each number to see if it's divisible by 11 or 13, and if it is, converts the number to a string, counts the occurrences of the digit '7', and adds this count to the total count. The final count is then returned. The script also includes test cases to verify the correctness of the function.