```python
def largest_divisor(n: int) -> int:
    return n if n == 1 else largest_divisor(n//2)
``` 
This function uses recursion to find the largest integer that divides a given number evenly, smaller than the given number.