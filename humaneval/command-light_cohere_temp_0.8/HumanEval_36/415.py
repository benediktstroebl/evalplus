```python
def fizz_buzz(n):
    return sum(i in str(n) for i in '771110')

# Test the function
assert fizz_buzz(50) == 0, "FizzBuzz failed"
assert fizz_buzz(78) == 2, "FizzBuzz failed"
assert fizz_buzz(79) == 3, "FizzBuzz failed"
```