```python
def change_base(x: int, base: int) -> str:
    """Change the base of a number x to a specified base."""
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")
        
    # handle negative numbers by converting to positive and shifting
    x = abs(x)
    return format(x, base=base)

# tests
test_change_base = []
test_change_base.push(1)
test_change_base.push(8)
test_change_base.push(16)
test_change_base.push(27)
test_change_base.push(28)
test_change_base.push(32)
test_change_base.push(100)
test_change_base.push(127)
test_change_base.push(35)
test_change_base.push(36)
test_change_base.push(70)
test_change_base.push(111)
test_change_base.push(82)
test_change_base.push(57)
test_change_base.push(63)
test_change_base.push(49)
test_change_base.push(97)
test_change_base.push(20)
```