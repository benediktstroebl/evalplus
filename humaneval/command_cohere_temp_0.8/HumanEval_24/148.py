```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number at index i can divide n evenly (i.e. n is divisible by i), then that number is returned. The loop ends after the check of the last number, ensuring there is no need for an additional check for n == 1, as the edge case is already handled.