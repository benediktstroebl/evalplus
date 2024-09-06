```python
def truncate_number(n):
    if n <= 1:
        return n
    i = 1
    while i <= int(n):
        n = n // 10
        i += 1
    return n

# Test cases from the docstring
print(truncate_number(3.5))
print(truncate_number(10))
print(truncate_number(0))
print(truncate_number(-10))
print(truncate_number(0.5))
print(truncate_number('12.5'))
```
This script defines a function `truncate_number` that takes a number as input and returns the decimal part of that number. The function uses a while loop to continuously divide the number by 10 until the remainder is less than 1. It returns the decimal part of the number.