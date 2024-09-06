```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not n % d), None)
``` 
This function uses the `next` function with a generator expression to find the largest number that divides the number n evenly, smaller than n. The function returns the time `None` if no such number was found.