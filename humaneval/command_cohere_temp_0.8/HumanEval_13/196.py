```python
def greatest_common_divisor(a, b) -> int:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The GCD algorithm leverages the property that the greatest common divisor of integers 'a' and 'b' is also the greatest common divisor of 'b' modulo 'a' and 'a' itself. This algorithm recursively replaces 'a' and 'b' with this pair until 'a' becomes 0 and returns 'b' as the greatest common divisor. 

Here's a concise version of the same algorithm:
```python
def greatest_common_divisor(a, b) -> int:
    return b if a == 0 else greatest_common_divisor(b%a, a)
```

This version stops recursing when 'a' is no longer 0 and returns 'b' as the GCD.