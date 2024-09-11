```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz(n)` that calculates the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a `for` loop to iterate over all numbers from 1 to `n-1`, checks if each number is divisible by 11 or 13, and increments the count by the number of occurrences of the digit 7 in the string representation of the number. The function then returns this count.

The test cases at the end of the script demonstrate the function's correctness by comparing its output with the expected output for specific inputs.