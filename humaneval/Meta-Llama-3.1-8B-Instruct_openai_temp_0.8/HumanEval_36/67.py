```python
def count_sevens(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n: A positive integer.
    
    Returns:
        An integer indicating the count of digit 7 in the required numbers.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n: A positive integer.
    
    Returns:
        An integer indicating the count of digit 7 in the required numbers.
    """
    return count_sevens(n)


# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `count_sevens` that counts the occurrences of the digit 7 in the numbers less than `n` which are divisible by 11 or 13. The function `fizz_buzz` is a wrapper around `count_sevens`. It uses the `str.count` method to count the occurrences of '7' in the string representation of the numbers. The test cases are included at the end to verify the correctness of the function.