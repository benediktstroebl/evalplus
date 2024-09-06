Here's the Python script with the self-contained function:
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer that divides n exactly
    """
    return max((i for i in range(1, int(n**0.25) if n % i == 0))
``` 
This function calculates the largest integer which divides the input number `n` without a remainder. It uses the efficient approach by iterating from 1 up to the square root of the input number, checking if the remainder is equal to 0.