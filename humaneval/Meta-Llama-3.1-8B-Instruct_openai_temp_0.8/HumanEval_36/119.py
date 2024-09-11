```python
def count_digit_7(n: int) -> int:
    """Count the occurrences of digit 7 in a number."""
    return str(n).count('7')


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(count_digit_7(i) for i in range(11, n) if i % 11 == 0 or i % 13 == 0) + \
           sum(count_digit_7(i) for i in range(13, n) if i % 11 == 0) + \
           sum(count_digit_7(i) for i in range(11, n) if i % 13 == 0)


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # 0
    print(fizz_buzz(78))  # 2
    print(fizz_buzz(79))  # 3
```

This script defines two functions: `count_digit_7` to count the occurrences of digit 7 in a number, and `fizz_buzz` to calculate the total count of digit 7 in numbers less than `n` which are divisible by 11 or 13. The test cases are included in the `if __name__ == "__main__":` block.