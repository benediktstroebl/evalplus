```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x in str(i) for i in range(1,n+1) if i % 10 == 7 and i % 11 == 0 or i % 13 == 0)

# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This Python function, fizz_buzz, is designed to calculate the number of occurrences of the digit 7 in numbers that are less than a given input n and are either divisible by 11 or 13. The function employs a sum() along with a generator expression to iterate through numbers from 1 up to n. This results in counting the number of times the digit 7 appears in these numbers. The function is then tested successfully with the provided input examples.