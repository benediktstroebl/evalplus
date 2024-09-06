```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function `largest_divisor(n)` takes an integer n as input and iterates through numbers from 1 to n-1. During iteration, it checks if the number is divisible by n and if so, returns that number which is also the largest divisor of n smaller than n.