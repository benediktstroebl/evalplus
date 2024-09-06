```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base base."""
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    return '{:0b}'.format(x, base)

# Test cases
assertEqual(change_base(8, 3), '22')
assertEqual(change_base(10, 3), '130')
assertEqual(change_base(12, 5), '248')
assertEqual(change_base(123, 2), '1111')
assertEqual(change_base(123, 10), '11000111')
assertEqual(change_base(123, 20), '200001111')
assertEqual(change_base(123456, 3), '83291323')
assertEqual(change_base(123456, 9), '666666')
assertEqual(change_base(123456, 12), '58691323')
assertEqual(change_base(123456, 21), '666665789')
assertEqual(change_base(123456, 22), '66666667777')
assertEqual(change_base(123456, 10), '56')
assertEqual(change_base(123456, 45), '14524291256')
```