### Fizz Buzz with Digit 7
```python
def count_sevens(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    
    def has_seven(num: int) -> bool:
        """Check if the digit 7 appears in the given number."""
        return '7' in str(num)

    return sum(1 for i in range(n) if (i % 11 == 0 or i % 13 == 0) and has_seven(i))


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_sevens(n)


if __name__ == "__main__":
    # Test cases
    print(fizz_buzz(50))  # Expected output: 0
    print(fizz_buzz(78))  # Expected output: 2
    print(fizz_buzz(79))  # Expected output: 3
```

This script first defines a helper function `has_seven` to check if the digit 7 appears in a given number. Then it defines the main function `count_sevens` to count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function `fizz_buzz` simply calls `count_sevens`. The test cases are executed when the script is run directly.