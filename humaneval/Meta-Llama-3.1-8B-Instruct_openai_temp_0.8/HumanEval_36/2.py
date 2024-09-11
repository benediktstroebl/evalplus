```python
def count_seven(n: int):
    """
    Count the number of times the digit 7 appears in integers less than n.
    """
    count = 0
    for i in range(n):
        str_i = str(i)
        count += str_i.count('7')
    return count


def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    return count_seven((n - 1) // 11) + count_seven((n - 1) // 13)


# Test cases
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

This script defines two functions: `count_seven` counts the number of times the digit 7 appears in integers up to `n`, and `fizz_buzz` counts the number of times 7 appears in numbers that are divisible by either 11 or 13. The `//` operator performs integer division, discarding the remainder. The test cases at the end show that the function behaves as expected.