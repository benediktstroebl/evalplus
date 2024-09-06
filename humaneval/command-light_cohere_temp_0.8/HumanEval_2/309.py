```python
def truncate_number(n):
    # Determine the maximum integer less than the number
    max_int = max(x for x in range(1, n))
    # Return the decimal part of the number
    return n - max_int

# Test the function
print(truncate_number(3.5))  # Expected output: 0.2
print(truncate_number(0.5))  # Expected output: 0.2
print(truncate_number(0.4))  # Expected output: 0.2
print(truncate_number(1))  # ZeroDivisionError
```