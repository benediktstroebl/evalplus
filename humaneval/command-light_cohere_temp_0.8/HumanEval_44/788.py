```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(5, 10)
    False
    """
    # 0 -> 1
    # 1 -> 10
    # 10 -> 100
    # ... -> n -> n * base^(n-1)
    n = x
    while n < base:
        n *= base
    return f"{n}"
```