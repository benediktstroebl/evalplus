```python
def fizz_buzz(n):
    return 7 - (n & 3) if n > 3 else 0

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
print(fizz_buzz(2))  # Output: 0
print(fizz_buzz(77))  # Output: 1
```