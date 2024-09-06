```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
``` 
This function employs a generator expression with the next() function to efficiently iterate through the numbers from 1 up to the given number n. It checks each number to see if it evenly divides n, returning the largest such number that satisfies this condition.