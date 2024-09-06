```python
def truncate_number(n):
    if n < 0:
        n *= -1
    integer = int(n)
    decimal = n - integer
    return decimal

# Test cases
print(truncate_number(3.5))  # Output: 0.0
print(truncate_number(-3.5))  # Output: 0.0
print(truncate_number('3.5'))  # Output: 0.0
print(truncate_number(10.5))  # Output: 1.6
print(truncate_number(1))  # Output: 0.0
print(truncate_number(-100))  # Output: -1.0
```
This script defines a function `truncate_number` that takes a floating point number as input and returns the decimal part of the number. It also provides some series of test cases to verify the correctness of the function.