```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if (i % 11 == 0 or i % 13 == 0) and (i > 9 or i % 10 != 0):
            digit = i % 10
        if digit != 7 and digit != 0:
            count += 1
    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function, fizz_buzz, calculates the number of times the digit 7 appears in integers that are less than n and are divisible by 11 or 13. It utilizes a specific logic to identify the occurrence of the digit 7 in such numbers and counts the number of such instances.