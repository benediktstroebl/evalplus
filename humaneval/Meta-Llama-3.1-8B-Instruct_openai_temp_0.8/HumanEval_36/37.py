```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit.

    Returns:
    int: The count of 7's in the specified range.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the count of the digit 7 in integers less than `n` that are divisible by 11 or 13. It iterates over the range from 1 to `n-1`, checks each number for divisibility by 11 or 13, and increments the count of 7's found in the string representation of each such number. The function then returns this count. The script includes test cases to verify its correctness.