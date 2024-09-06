```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
We've created a function that calculates the largest integer which evenly divides a given number n. This function uses the blueprint to iterate through the numbers 1 to n, and checks if the remainder of n divided by each number is 0. The first number that satisfies the criteria to be the largest_divisor.