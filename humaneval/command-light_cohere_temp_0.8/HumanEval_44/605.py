```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    if base == 10:
        return str(x)
    elif base == 2:
        return str(x, base=12)
    else:
        return str(x, int(base))

x = 8
test_change_base = change_base(x, 2)
print(test_change_base)
```