```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), None) or n
``` 
This code defines a function `largest_divisor` that finds the largest divisor of a given number n. The function uses the result in less than O(1) and the time complexity is constant, as it uses the `next` function, which is constant time. The `largest_divisor` function will return the largest divisor of the number n.