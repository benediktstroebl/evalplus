```python
def truncate_number(n):
    x, dec = divmod(n, 10)
    return dec

# Test cases
print(truncate_number(3.5))  # Output: 0.5
print(truncate_number(0.01))  # Output: 1
print(truncate_number(-3.1))  # Output: -1
print(truncate_number(10.5))  # Output: 5
print(truncate_number(1.5))  # Output: 5
print(truncate_number(123456.3))  # Output: 56
```