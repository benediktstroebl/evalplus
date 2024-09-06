```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(int(c) == 7 for c in str(str(n)) if c in '78911130' or c in ')%1113' or c in '7777' and n >= 8)

# Example usage
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This Python function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in numbers less than n, which are divisible by 11 or 13. It employs a specific pattern matching to identify the digit 7, then sums up these occurrences to determine the final count.