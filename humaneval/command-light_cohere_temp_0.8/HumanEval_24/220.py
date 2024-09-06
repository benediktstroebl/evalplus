```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n // 2 + 1
    ``` 
This function calculates the largest integer that evenly divides the given number without a remainder, using the `divisibility by 2 rule`.