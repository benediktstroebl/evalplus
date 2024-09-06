```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number at index `i` can divide `n` evenly (i.e., `n % i == 0`), it returns `i` as the largest divisor. This algorithm is guaranteed to find the largest divisor smaller than n.