```python
def count_sevens(num: int) -> int:
    """Count the number of times the digit 7 appears in a given number."""
    count = 0
    for digit in str(num):
        if digit == '7':
            count += 1
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_sevens(i)
    return count


# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script first defines a helper function `count_sevens` that counts the number of times the digit 7 appears in a given number. Then it defines the main function `fizz_buzz` which uses this helper function to count the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13. Finally, it includes some test cases to demonstrate the function's correctness.