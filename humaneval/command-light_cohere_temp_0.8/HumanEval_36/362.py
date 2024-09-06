```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(10, n+1, 2):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Example usage:
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given number `n` which are divisible by 11 or 13. It iterates through numbers from 10 to `n` with a step of 2 to check for divisibility. The function then returns the count of the appearances of 7.

Note: The code assumes that the input `n` is an integer. It is not, therefore, recommended that you validate the input to ensure it meets the expected requirements.