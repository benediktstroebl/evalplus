```python
def string_sequence(n: int) -> str:
    if n < 0:
        raise ValueError("n should be non-negative")
    return f"0 {n}"*len(str())
```