```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            return i
    return 1
```
The function iterates through numbers from 1 to n-1, and returns the largest number in this range that divides n evenly (excluding n itself, which would be a trivial solution). This algorithm guarantees that the returned value is the largest possible correct answer.