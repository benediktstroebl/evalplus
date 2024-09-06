```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
``` 
This function uses the 'next' function to iterate through numbers from 1 up to the given number 'n', and checks if the number divides 'n' evenly (i. Then, it returns the finally, which is the largest such divisor.