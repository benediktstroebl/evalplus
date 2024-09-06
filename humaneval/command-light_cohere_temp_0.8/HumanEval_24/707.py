```python
def largest_divisor(n: int) -> int:
    return (n//2 + 1) if n % 2 == 0 else (n + 1)
    ```