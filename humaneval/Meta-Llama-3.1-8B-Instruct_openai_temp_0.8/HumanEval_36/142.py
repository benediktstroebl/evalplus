```python
def count_seven(n: int) -> int:
    """Return the number of times the digit 7 appears in the integer less than n which is divisible by 11 or 13."""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_seven(n)

if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

In this script, the `count_seven` function calculates the number of appearances of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The `fizz_buzz` function is a wrapper for `count_seven` and is used for testing purposes. The `if __name__ == "__main__":` block is used to run the tests when the script is run directly (not when it's imported as a module).