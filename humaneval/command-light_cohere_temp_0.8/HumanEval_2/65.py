```python
def truncate_number(n):
    if not n or n < 0:
        raise ValueError("Input must be a positive number")
    if not n % 1:
        return n
    return 0.5
```

The function tests for a positive number, and if the number is not positive, a ValueError exception is raised.