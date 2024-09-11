```python
def count_sevens(n: int) -> int:
    """Count the number of times the digit 7 appears in numbers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sevens(n)

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script first defines a helper function `count_sevens` that iterates over all numbers less than `n`, checks if they are divisible by 11 or 13, and counts the occurrences of the digit 7. The `fizz_buzz` function simply calls `count_sevens` and returns its result. The test cases are included at the end to verify the correctness of the `fizz_buzz` function.