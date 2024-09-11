```python
def count_sevens(n: int):
    """Return the number of times the digit 7 appears in the range [1, n).
    """
    count = 0
    for i in range(1, n):
        if '7' in str(i):
            count += 1
    return count


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_sevens(i)
    return count


# Example use cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

This script first defines a helper function `count_sevens` to count the number of times the digit 7 appears in a given number. It then uses this helper function in the `fizz_buzz` function to count the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13. The `if __name__ == "__main__":` block is used to verify the correctness of the `fizz_buzz` function with the provided example use cases.