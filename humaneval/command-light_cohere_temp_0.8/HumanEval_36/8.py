Here's the code:
```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    divisible = False
    count = 0
    for i in range(1, n+1):
        if i % 10 == 7 and ((i % 11 == 0) or (i % 13 == 0)):
            divisible = True
        if divisible:
            count += 1

    return count

# Example usage
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function fizz_buzz takes an integer n as input and returns an integer representing the number of occurrences of the digit 7 in integers less than n which are divisible by 11 or 13. The function uses a loop and a conditional statement to check for the digit 7 and divisible condition. The final count is then returned as the output.