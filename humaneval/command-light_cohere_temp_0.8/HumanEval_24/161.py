```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d), 1)
``` 
This function uses the `next()` function with a generator expression to generate numbers from 1 up, checks if they divide the input n evenly (meaning their remainder is 0), and returns the largest such divisor. 
This is a self-contained and efficient solution to find the largest divisor of a given number n.