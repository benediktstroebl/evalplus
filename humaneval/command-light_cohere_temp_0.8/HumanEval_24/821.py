```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
```
We've used the 'next' function with a generator expression to achieve iteration with a single pass over the numbers from 1 to 'n'.  The 'range' function was used for the generator expression to create a sequence of numbers less than 'n'.  The 'largest_divisor' function returns the largest number that divides 'n' without a remainder.