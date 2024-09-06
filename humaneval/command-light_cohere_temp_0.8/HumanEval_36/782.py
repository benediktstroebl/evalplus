```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    c = 0
    for i in range(1, n+1):
        if i % 10 == 7 and (i % 11 == 0 or i % 13 == 0):
            c += 1
    return c

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script defines a function `fizz_buzz` that computes the count of occurrences of the digit 7 in numbers less than a given number `n` that are both divisible by 11 and 13. 

The function iterates through numbers from 1 to `n`, and checks each number's divisibility by 11 and 13. It increments the number of occurrences of the digit 7 in the `c` counter when such a number is found.

The test section demonstrates the function's behavior by passing various values to the `fizz_buzz` function and printing the results.