```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The count of occurrences of the digit 7.
    """
    count = 0
    for i in range(11, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script works by iterating over numbers from 11 to `n-1` (inclusive), checking if each number is divisible by 11 or 13, and if so, counting the occurrences of the digit '7' in its string representation. The total count of occurrences is then returned.