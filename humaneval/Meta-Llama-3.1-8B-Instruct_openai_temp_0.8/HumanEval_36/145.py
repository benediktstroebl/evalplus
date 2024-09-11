```markdown
### Fizz Buzz Problem Solution

This Python script solves the Fizz Buzz problem, where we need to count the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

#### Code
```python
def count_sevens(numbers):
    """Return the count of digit 7 in the given list of numbers."""
    return sum(str(num).count('7') for num in numbers)


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_sevens([i])
    return count
```

#### Example Usage
```python
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

#### Explanation
This solution uses a helper function `count_sevens` to count the occurrences of the digit 7 in a list of numbers. The `fizz_buzz` function iterates over all numbers less than `n`, checks if they are divisible by 11 or 13, and uses the `count_sevens` function to count the occurrences of 7 in those numbers.
```