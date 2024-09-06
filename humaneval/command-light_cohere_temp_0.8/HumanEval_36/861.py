```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(i for i,d in enumerate(str(str(n))[d=='7])) % 2

# Example usage:
print(fizz_buzz(50))  # Output:  0
print(fizz_buzz(78))  # Output:  2
print(fizz_buzz(79))  # Output:  3
```
The function fizz_buzz uses the enumerate function to loop over each character in the string representation of n, and checks if the character is '7'. The function returns the number of such characters, and this number is then divided by 2 to ensure that the result is non-negative.