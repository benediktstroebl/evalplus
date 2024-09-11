```python
def count_seven(n: int) -> int:
    """Helper function to count the occurrences of digit 7 in a given number."""
    return str(n).count('7')


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_seven(i)
    return count


# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines two functions: `count_seven` counts the occurrences of digit 7 in a given number, and `fizz_buzz` counts the occurrences of digit 7 in integers less than `n` which are divisible by 11 or 13. The test cases at the end demonstrate the function's behavior as expected.