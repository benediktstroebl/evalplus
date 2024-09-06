```python
def largest_divisor(n: int) -> int:
    return (n//2 + 1) if n % 2 != 0 else (n+1)
    ``` 
This code defines a function named largest_divisor that takes an integer n as input and finds the largest divisor of n. It does this using a test cases by checking if the input n is even or odd, and returns the largest divisor accordingly, which is always greater than or equal to n/2.