```python
def truncate_number(n: float) -> float:
    if not n.is_positive():
        raise ValueError("Input must be a positive number")

    result = n // int(n)
    return result if result <= 1 else 0.0
```