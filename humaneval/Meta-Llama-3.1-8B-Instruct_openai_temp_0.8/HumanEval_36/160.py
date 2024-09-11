```python
def count_sevens_less_than_n(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sevens_less_than_n(n)

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This Python script defines a function `fizz_buzz(n)` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses another helper function `count_sevens_less_than_n(n)` to count the occurrences of the digit 7. The script includes test cases to demonstrate the function's correctness.