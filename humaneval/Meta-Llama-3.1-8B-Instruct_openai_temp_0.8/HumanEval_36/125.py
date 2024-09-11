```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(n-1, 0, -1):
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
This Python script defines the `fizz_buzz` function to solve the problem. It iterates over all integers from `n-1` down to 1, and checks if each integer is divisible by 11 or 13. If it is, it converts the integer to a string and checks each digit. If the digit is 7, it increments the count and breaks the loop. Finally, it returns the count. The test cases are included at the end of the script to verify the function's correctness.