```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be an integer")

    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")

    if base == 2:
        return f"{x:02}"
    elif base == 10:
        return f"{x:03}".center(3)
    else:
        return str(f"{x: {base}"}
    ```