```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    # use floor division to get rid of floating decimal when there is only one
    # common divisor left
    while a % b == 0 and b != 0:
        a //= a // b
        b //= a % b
    return a // b
```