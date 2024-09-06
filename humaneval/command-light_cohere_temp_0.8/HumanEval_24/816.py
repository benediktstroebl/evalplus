Here's the self-contained Python function that finds the largest divisor of a given number: 

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest divisor of the number, ensuring it divides evenly."""
    while n % 2 == 0:
        n /= 2
    return n
``` 

This function uses a while loop to repeatedly divide the number by 2 until it is odd, at which point the loop terminates and the divisibility is achieved.