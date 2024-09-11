```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

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
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a for loop to iterate over all integers less than `n`, checks for divisibility by 11 or 13, converts the number to a string, and counts the occurrences of the digit 7. The function returns the total count. The test cases at the end verify the function's correctness.