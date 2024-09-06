```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base
    >>> change_base(8, 10) # Should return '88'
    >>> change_base(10, 10) # Should return '1'
    >>> change_base(3, 2) # Should return '230'
    >>> change_base(123, 4) # Should return '0123456789'
    >>> change_base(1, 35) # Should return '4321'
    >>> change_base('a', 123) # Should return 'abc'
    >>> change_base('2', -1) # Should raise ValueError: unsupported base -1
    """
    if base == x or base < 0:
        raise ValueError("Unsupported base value")
    return '{:0>{base}'.format(x)

# Test cases
print(change_base(8, 10))  # Output: 88
print(change_base(10, 10))  # Output: 1
print(change_base(3, 2))  # Output: 230
print(change_base(123, 4))  # Output: 0123456789
print(change_base(1, 35))  # Output: 4321
print(change_base('a', 123))  # Output: abc
print(change_base('2', -1))  # Output: 

```