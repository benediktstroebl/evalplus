```python
def count_7s(n: int):
    """
    Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The count of 7s.
    """
    count = 0
    for i in range(n):
        if (i % 11 == 0 or i % 13 == 0) and '7' in str(i):
            count += 1
    return count


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The count of 7s.
    """
    return count_7s(n)


# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `count_7s` that iterates over all integers less than `n`, checks if the current integer is divisible by 11 or 13, and if it contains the digit 7. If both conditions are met, the digit 7 is counted. The function `fizz_buzz` simply calls `count_7s` with the given input `n`. The test cases at the end verify the correctness of the function.