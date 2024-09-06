```python
def truncate_number(n: float) -> float:
    return n if n.isdigit() else 0.5
    aspect of n, else 1e

#Test cases
print(truncate_number(123.456)) # Output: 2
print(truncate_number(123.456.8)) # Output: 1
print(truncate_number(123.456)) # Error: ValueError: invalid literal for int() with base 10
print(truncate_number('a123.456')) # Output: 1
print(truncate_number(123e5)) # Error: ValueError: invalid literal for int() with base 10
print(truncate_number(1e+100)) # Error: ValueError: invalid literal for int() with base 10
print(truncate_number('a3')) # Error: ValueError: invalid literal for int() with base 10
```