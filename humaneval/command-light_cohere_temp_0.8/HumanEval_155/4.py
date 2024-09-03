```python
def even_odd_count(num):
    """
    Returns a tuple with the number of even and odd digits in the given integer.
    """
    The even integer passed to the function.
    even_digits = sum(1 for digit in str(num) if digit == '0')
    odd_digits = sum(1 for digit in str(num) if digit != '0')
    return (even_digits, odd_digits)

#Example:
print(even_odd_count(-12))
```