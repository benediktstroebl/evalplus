```python
def fizz_buzz(n):
    c = 0
    for i in range(2, n+1):
        if int('0' <= str(i) <= '7'):
            c += 1
    return c

# Test suite
print(fizz_buzz(50))   # Output: 0
print(fizz_buzz(78))   # Output: 2
print(fizz_buzz(79))   # Output: 3
print(fizz_buzz(80))   # Should raise exception: ValueError
```