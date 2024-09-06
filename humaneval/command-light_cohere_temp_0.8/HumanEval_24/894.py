```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not any(n % d == 0))
``` 
This Python function, largest_divisor, calculates and returns the largest integer divisor of the given number n that does not leave any remainder. The code uses a strongest technique of elimination, by testing all numbers from 1 up to see if any divides the number evenly.