```python
def iscube(a):
    # Check if the number is divisible by 2 and then 3
    return not a & 1 and not a & 3
```

The function checks if the number `a` is divisible by 2 and 3 by using bit operations. 

For the bit operation `not a & 1`, the result is `True` if the least significant bit is zero, meaning that the number is divisible by 2.

Similarly, the bit operation `not a & 3` checks if the least significant two bits are zero, which means that the number is divisible by 3. 

Since a perfect cube number can be expressed as `n * n * n`, it must be divisible by 2 and 3. Hence, with this check, the function returns `True` if `a` is a cube and `False` otherwise. 

This solution has a time complexity of `O(1)` since it only takes one bitmask operation to determine the result.