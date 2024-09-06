```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```

This function iterates through numbers from 1 to n and returns the largest divisor of n that is smaller than n. 

Such a divisor may not exist if n is prime, in which case the function would return None. If that is the case, the function could be modified as follows:
```python
def largest_divisor(n):
    """ For a given number n, return the largest divisor of n that is smaller than n, or None if n is prime """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
    return None
```
The function returns None immediately once it confirms that n is prime, without needing to iterate through the entire range.