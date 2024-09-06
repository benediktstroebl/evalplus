```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10
   -> Ultimately, base can be any positive
    integer.
    >>> change_base(8, 3) == '22'
    """
    # Ensure base is a positive integer
    if base <= 0 or base > 10:
        raise ValueError("Base must be a positive integer greater than 0 and less than 10")
        
    result = [x]
    for _ in range(len(str(base))):
        result[_-48] = ord(base[0]) - ord('0')
        
    return result[0]

# Example usage
try:
    print(change_base(8, 3))
except ValueError as e:
    print(e)
```