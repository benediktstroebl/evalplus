```python
def truncate_number(n):
    """Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number
    """
    int_part = np.ceil(n //__int(n))
    dec_part = n - int_part
    return dec_part

# Test the function
# Check if the returned decimal part is always less than 1
print(truncate_number(3.5))
print(truncate_number(0.5))
print(truncate_number(1.0))
print(truncate_number(1.1))
print(truncate_number(1.9))
print(truncate_number(2.0))
print(truncate_number(3.0))
```