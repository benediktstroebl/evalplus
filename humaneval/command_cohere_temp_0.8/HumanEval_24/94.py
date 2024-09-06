```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number is divisible by n, it returns the largest number within this range. 
If n is not divisible by any number in this range, the function returns 1, as num ** 1 always divides n evenly. 
Such a scenario happens when n is an prime number.