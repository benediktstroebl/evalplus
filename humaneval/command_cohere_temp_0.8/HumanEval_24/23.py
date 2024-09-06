```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number at index i can divide n evenly (i.e. n is divisible by i), then that number is returned. The loop ends after the largest possible divisor is found, so no need to go through the entire range (as evidenced by thelack of a range(n+1) iteration).