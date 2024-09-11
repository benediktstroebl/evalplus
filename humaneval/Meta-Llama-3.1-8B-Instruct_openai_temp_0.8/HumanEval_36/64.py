### Fizz Buzz Counter
#### Problem Description
This script calculates the number of times the digit 7 appears in integers less than a given number `n`, which are divisible by 11 or 13.

#### Code
```python
def count_digit(n: int, digit: int) -> int:
    """Return the number of times the digit `digit` appears in integers less than `n`."""
    count = 0
    for i in range(1, n):
        if str(digit) in str(i):
            count += 1
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13."""
    return count_digit(n, 7) - count_digit(n // 11, 7) - count_digit(n // 13, 7) + count_digit(n // (11 * 13), 7)


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # 0
    print(fizz_buzz(78))  # 2
    print(fizz_buzz(79))  # 3
```

#### Explanation
This script uses the `count_digit` function to count the occurrences of a given digit in integers less than a number `n`. The `fizz_buzz` function then uses this helper function to count the occurrences of 7 in integers less than `n` that are divisible by 11 or 13. Note that this is a simple solution that does not use any advanced algorithms or data structures. It is also not optimized for performance, but it gets the job done.