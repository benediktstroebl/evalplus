```python
def count_sixes(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sixes(n)

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a function `count_sixes` which counts the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The function `fizz_buzz` simply calls `count_sixes` to provide a more descriptive name in line with the problem description. The script then includes test cases to demonstrate the correctness of the solution.