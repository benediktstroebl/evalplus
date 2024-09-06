```python
def fizz_buzz(n: int):
    return len([i for i in range(1, n+1) if any(x % 15 == 7 for x in str(i+0)))

# Test the function
assert(fizz_buzz(50), 0)
assert(fizz_buzz(78), 2)
assert(fizz_buzz(79), 3)
```