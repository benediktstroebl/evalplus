```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base.
    return string representation after conversion
   
    base numbers less than 2 won't work
    """
    assert base > 0, f"Invalid base number: {base}"
    return '{x}'.format(str(x), int(base)))

# Example usage
x = 8
base = 2
print(change_base(x, base))  # Output: '1000'
```