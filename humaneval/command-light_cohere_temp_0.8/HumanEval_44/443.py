```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Invalid input types. Ensure both x and base are integers.")
    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Base must be between 2 and 36.")
    if x < 0:
        raise ValueError("Input number must be positive.")
    
    if base == 10:
        return f"{x:d}"
    elif base == 2:
        return f"{x:02}"
    elif base == 16:
        return f"{x:04}"
    elif base == 22:
        return f"{x:07}"
    elif base == 11:
        return f"{x:09}"
    elif base == 1011:
        return f"{x:11}"
    else:
        return str(f"{x:d} base {base}")
    
    # Additional tests
    if not str(x) == f"{x:d} base {base}":
        raise ValueError("Incorrect output format.")
    if base < 2 or base > 36 or not isinstance(x, int):
        raise ValueError("Invalid input types.")
```