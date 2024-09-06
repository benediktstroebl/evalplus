```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n + 1) if not any(n % x == 0)) - 1)
```
This function uses the Python next() function with a generator expression to iterate over numbers from 1 up to the given number n, checks if any of these numbers divide n evenly, and returns the largest such number less than n.