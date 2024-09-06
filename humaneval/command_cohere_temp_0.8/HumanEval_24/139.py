```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number at index i can divide n evenly (i.e., n is divisible by i), then that number is returned. The loop ends as soon as such a number is found, guaranteeing that the function will not iterate through unnecessary numbers. This approach guarantees efficiency in finding the largest divisor smaller than n.