```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number x to base base.
    :return string representation after conversion
    """

    :param x: int, input number
    :param base: int, input base
    :return: string, base converted representation
    """
    if base == 10:
        return str(x)
    return '{:0{}{}'.format(x, base)

# Tests
print(change_base(8, 3))      # Expected output: '22'
print(change_base(5, 2))      # Expected output: '1000'
print(change_base(7, 2))      # Expected output: '111'
print(change_base(0, 7))      # Expected output: '00110'
print(change_base(12, 35))     # Expected output: '301070080010'
print(change_base(93, 16))   # Expected output: '600162304'
```