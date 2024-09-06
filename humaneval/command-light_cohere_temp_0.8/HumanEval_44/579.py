```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base B"""
    assert base > 0, "Base number should be greater than 0"
    result = [2 ** i for i in range(base)]
    return str(x // result)

print(change_base(8, 2)) # Output should be '1000'
print(change_base(7, 3)) # Output should be '22'
print(change_base(-8, 2)) # Base number should be greater than 0
```