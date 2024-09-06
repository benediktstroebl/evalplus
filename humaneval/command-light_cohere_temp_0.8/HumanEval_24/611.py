```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer which divides n exactly without a remainder.
    """
    def is_divisible(x: int) -> bool:
        return all(i divides x for i in range(1, int(x**0.5)))
    def largest_divisor(n):
        return max(x for x in range(1, n+1) if is_divisible(x))
    ```