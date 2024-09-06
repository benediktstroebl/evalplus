```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n + 1) if any(x % i == 0 for i in range(1, n+1)) ))
```
Do you require assistance with any other Python-related tasks? I can help you solve other problems or clarify more concepts.