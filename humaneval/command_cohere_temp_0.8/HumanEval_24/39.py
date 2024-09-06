```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            return i
    return 1
```
The function iterates through numbers from 1 to n-1, checking if the current number evenly divides n. The fastest dividing integer that is less than n is returned. 

This algorithm is efficient because it uses the property that the greatest common divisor will always be the smallest among all possible divisors. 

Would you like assistance with any other coding problems or concepts?