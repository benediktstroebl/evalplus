```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    # Perform the conversion
    s = str(x)
    return s if s.iscode(s, 10, base) else s
```
Do you require assistance with any other Python coding problems or want to explore other coding concepts?