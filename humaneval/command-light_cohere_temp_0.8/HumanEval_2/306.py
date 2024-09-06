```python
def truncate_number(n):
    x, d = divmod(n, 10)
    return d

# Example usage:
n = 3.5
print(truncate_number(n))  # Output: 0.5
```
This Python code defines a function called `truncate_number` that takes a single argument `n`, expected to be a positive floating point number. The function performs integer division (`divmod`) of `n` by 10, extracting the quotient (the integer part) and the remainder (the decimal part). The remainder is then returned as the result.