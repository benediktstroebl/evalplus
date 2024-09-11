```python
def count_sevens(n: int):
    """Count the number of times the digit 7 appears in the range [start, n).
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_sevens(n)


if __name__ == "__main__":
    # Test the fizz_buzz function
    print(fizz_buzz(50))  # Expected output: 0
    print(fizz_buzz(78))  # Expected output: 2
    print(fizz_buzz(79))  # Expected output: 3
```

This script first defines a helper function `count_sevens(n)` that counts the occurrences of the digit 7 in the numbers from 0 to `n-1`. It then defines the main function `fizz_buzz(n)` that uses `count_sevens(n)` to count the occurrences of the digit 7 in the numbers from 0 to `n-1` that are divisible by 11 or 13. Finally, it tests the `fizz_buzz` function with some sample inputs.