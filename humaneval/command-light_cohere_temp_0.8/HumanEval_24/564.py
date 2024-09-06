```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that divides n exactly
    """
    return next((d for d in range(1, int(n**0.25)) if n % d == 0)
``` 
This function employs the generator expression to generate all integers from 1 up until the square root of the input number n, ensuring that each integer d divides n exactly. The function returns the specific number d which satisfies this condition.