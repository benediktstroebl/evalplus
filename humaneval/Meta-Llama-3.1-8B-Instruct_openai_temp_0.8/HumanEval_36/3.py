```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit (exclusive) for checking integers.

    Returns:
    int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(11, n):  # start from 11 because we need numbers divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the count of digit 7 appearing in integers less than `n` that are divisible by 11 or 13. The function uses a loop to iterate through the range from 11 to `n` (exclusive), and checks each number to see if it's divisible by 11 or 13. If it is, the function counts the occurrences of the digit 7 in the number. Finally, it returns the total count.