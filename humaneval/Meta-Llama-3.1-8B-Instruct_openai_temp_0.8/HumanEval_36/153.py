```python
def count_sixes(n: int) -> int:
    """Count the occurrences of the digit 6 in numbers divisible by 6 less than n."""
    count = 0
    for i in range(n):
        if i % 6 == 0:
            str_i = str(i)
            count += str_i.count('6')
    return count

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

In this script, the `fizz_buzz` function iterates through all integers less than `n`, checks if they are divisible by 11 or 13, and counts the occurrences of the digit 7 in their string representation. The `count_sixes` function is not used in the `fizz_buzz` function as per your specification, but I included it for completeness.