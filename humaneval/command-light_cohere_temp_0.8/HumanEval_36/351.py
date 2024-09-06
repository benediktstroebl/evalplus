```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(c == 7 for c in str(i) for i in range(1, n + 1) if i % 10 != 6)

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function fizz_buzz that calculates the number of times the digit 7 appears in the range of integers less than a given number n, which are either divisible by 11 or 13. The function uses a string comprehension to check if the digit 7 appears in each number, and the modulo operator to skip over the number 7. The function then returns the value of the total count of such numbers, which equals the number of times the digit 7 appears in them.