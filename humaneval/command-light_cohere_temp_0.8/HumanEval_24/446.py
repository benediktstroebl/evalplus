```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number divisible by n that is less than n"""  
    return n // max(n, int(n ** 0.25))
```
This code defines a function called largest_divisor that takes an integer n as input and returns the largest number divisible by n that is less than n. 

The code uses a concise and readable definition for the purpose of the function, which is to find the largest divisor of n.