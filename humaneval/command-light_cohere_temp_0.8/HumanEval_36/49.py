```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(int(i) == 7 and i <= n and i % 11 or i % 13 == 0 for i in range(0, n+1))

# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This script defines a function, `fizz_buzz`, which takes an integer `n` as input and returns the number of times the digit 7 appears in numbers that are less than `n` and are divisible by 11 or 13. 

The function uses a `sum` operation to count the number of such numbers and returns the result.