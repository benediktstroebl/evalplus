```python
def count_sevens(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n - 1, 0, -1):
        # Check if i is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to count the digit 7
            count += str(i).count('7')
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sevens(n)


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))
    print(fizz_buzz(78))
    print(fizz_buzz(79))
```

This script defines two functions, `count_sevens` and `fizz_buzz`. The `fizz_buzz` function is just a wrapper that calls the `count_sevens` function. The `count_sevens` function iterates over all numbers less than `n`, checks if they are divisible by 11 or 13, and counts the occurrences of the digit 7 in their string representation. The results of the test cases are printed to the console.