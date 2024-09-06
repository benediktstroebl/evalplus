Here's the Python script with the self-contained function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    return next((d for d in x if n % d == 0 and d != 0), n)
```
This function takes an integer n as input and returns the largest divisor of n. It uses the testing for a list of divisors of n and uses the next() function to get the largest divisor which divides the number evenly and is smaller than n. The returned value is the largest divisor.