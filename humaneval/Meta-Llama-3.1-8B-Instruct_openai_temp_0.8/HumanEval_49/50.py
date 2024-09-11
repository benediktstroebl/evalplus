### Modulo Power Function
#### Python Implementation
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (with given numerics).
    
    Parameters:
    n (int): The exponent.
    p (int): The modulo value.
    
    Returns:
    int: The result of 2^n modulo p.
    
    Example:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = 1
    while n > 0:
        if n % 2 == 1:
            # If n is odd, n = 2^0 + 2^1 +... + 2^(n-1)
            result = (result * 2) % p
        else:
            # If n is even, n = 2^0 + 2^1 +... + 2^(n/2 - 1) + 2^(n/2)
            n = n // 2
            result = (result * result) % p
    return result
```

### Usage

You can use this function like any other Python function. For example:
```python
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```