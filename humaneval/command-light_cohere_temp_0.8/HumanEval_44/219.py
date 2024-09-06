```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base B"""
    if base <= 0 or base >= 5:
        raise ValueError("Base must be between 1 and 5.")
    return f"{x}_{base}"

def test_change_base():
    try:
        print(change_base(8, 2))
        print(change_base(7, 3))
        print(change_base(123, 1))
        print(change_base(-7, 2))
        print(change_base(0, 10))
    except ValueError as e:
        print(f"Error: {e}")
```