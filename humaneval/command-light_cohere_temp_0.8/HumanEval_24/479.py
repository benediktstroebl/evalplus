```python
def largest_divisor(n: int) -> int:
    """Finds the largest integer which divides the given number evenly"""
    return next((d for d in range(1, int(n**0.5)) if n % d == 0)
```
Do you require any further assistance with code implementation or have other questions related to specific algorithms or concepts?