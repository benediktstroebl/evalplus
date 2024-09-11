```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit for the integers to be checked.
    
    Returns:
    int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            for digit in str(i):
                if digit == '7':
                    count += 1
                    break
    return count


# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz(n)` that checks each integer less than `n` to see if it is divisible by 11 or 13. If it is, it converts the integer to a string and checks each character (digit) to see if it is '7'. If it is, it increments the `count` variable. Finally, it returns the `count`.