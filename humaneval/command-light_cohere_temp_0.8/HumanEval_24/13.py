```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n + 1) if all(x % n == 0)))
```
The function returns the largest integer that divides the given number n exactly or evenly, ensuring the greatest possible factor that fits without remainder. 

I hope this helps your problem!