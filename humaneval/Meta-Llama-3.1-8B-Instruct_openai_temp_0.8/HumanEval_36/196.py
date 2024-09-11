```python
def count_sevens(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sevens(n)


# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

In this script, the `count_sevens` function is used to count the occurrences of the digit 7 in integers less than `n` which are divisible by 11 or 13. The `fizz_buzz` function simply calls `count_sevens` to achieve the same result. The test cases at the end verify the correctness of the `fizz_buzz` function.