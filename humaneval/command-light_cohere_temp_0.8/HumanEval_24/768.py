```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n, 
    that divides n exactly without a remainder.
    """
    if not n ordivisible():
        return n
    lcm = n*((n-1)//2)
    i = 2
    while i*i <= lcm:
        if lcm%i == 0:
            return i
    return 2*i-1
``` 
This function, largest_divisor, calculates the largest integer less than n that divides n exactly, without a remainder. It does this by using the condition to start the loop: if the least common multiple (LCM) of n and i is divisible by i, then i is the largest divisor.