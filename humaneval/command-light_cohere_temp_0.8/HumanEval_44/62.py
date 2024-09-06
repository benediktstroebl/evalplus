```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    """
    if x < 0 or base < 2:
        raise ValueError("Input value or base should be positive")
    result = []
    while x > 0:
        remainder = x % base
        result.append(remainder)
        x //= base
    return ''.join(map(lambda x: f"{x:02}", result))

def test_change_base():
    base = 2
    x = 7
    expected = '111'
    result = change_base(x, base)
    assert result == expected, f"Failed, got {result}, expected {expected}"

test_change_base()
print("Test passed!")
```