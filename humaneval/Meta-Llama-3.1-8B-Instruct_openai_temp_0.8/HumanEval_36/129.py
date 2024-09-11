```markdown
## Fizz Buzz Counter

This script counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

### Code
```python
def count_digit(n: int, digit: int):
    """Return the number of times a given digit appears in n."""
    return str(n).count(str(digit))


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit(i, 7)
    return count


# Example use cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

### Explanation

This script first defines a helper function `count_digit(n, digit)` that counts the occurrences of a given digit in a number `n`. It converts the number to a string to easily count the occurrences of the digit.

The main function `fizz_buzz(n)` iterates over all numbers less than `n`, and checks if they are divisible by 11 or 13. If a number is divisible by either of these numbers, it adds the count of the digit 7 in that number to the total count.

Finally, the script includes example use cases to demonstrate the function's behavior.

### Time Complexity

The time complexity of this script is O(n), where n is the input number. This is because we need to iterate over all numbers less than n to check for divisibility and count the digit 7.