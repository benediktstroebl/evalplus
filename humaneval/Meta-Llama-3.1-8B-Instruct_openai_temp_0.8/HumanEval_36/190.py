```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit of integers to check.
    
    Returns:
        int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a loop to iterate over all integers less than `n`, checks if each integer is divisible by 11 or 13 using the modulo operator, and increments a counter each time it encounters a number containing the digit 7. Finally, the function returns the total count.

The script includes test cases to verify the correctness of the `fizz_buzz` function.