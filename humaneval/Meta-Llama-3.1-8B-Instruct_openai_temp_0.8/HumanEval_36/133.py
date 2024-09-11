```python
def count_sevens(n: int) -> int:
    """Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n-1, 0, -1):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sevens(n)


# Example usage
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

In this script, the `count_sevens` function iterates over integers less than `n` in reverse order, checking each integer for divisibility by 11 or 13. It counts the occurrences of the digit '7' in the string representation of each integer. The `fizz_buzz` function simply calls `count_sevens` to calculate the count.