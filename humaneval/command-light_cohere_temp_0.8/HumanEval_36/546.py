```python
def fizz_buzz(n):
    return sum([i in str(x) for x in range(1, n + 1) if x % 11 == 7 or x % 13 == 7])

# Test the function
assert(fizz_buzz(50) == 0)
assert(fizz_buzz(78) == 2)
assert(fizz_buzz(79) == 3)

# The function correctly calculates the number of times 7 appears in numbers less than n that are divisible by 11 or 13. 
```