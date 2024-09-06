```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to the base B.

    :Applicable bases: 10, 2, and 10 are supported.
    """if base not match '10':
        return str(x)
    elif base == 2:
        return ''.join(str(x) for x in str(x, 10))
    elif base == 10:
        return ''.join(str(x) for x in str(x, 2))
    else:
        raise ValueError("Invalid base value. Base must be 10, 2 or Base.")

    return ''

# Example usage
x = 8
base = 3
result = change_base(x, base)
print(result)

# Test cases
print(change_base(8, 10)) # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(8, 20)) # Output: Must raise ValueError
```