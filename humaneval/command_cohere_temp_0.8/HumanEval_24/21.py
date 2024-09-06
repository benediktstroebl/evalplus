```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number is divisible by n, it returns the number itself. If not, it moves to the next number. The iteration stops when the test condition `n % i == 0` is satisfied, which ensures that the returned value is truly a divisor of n. As the loop runs up to `n`, it also guarantees that the returned value will be smaller than n.