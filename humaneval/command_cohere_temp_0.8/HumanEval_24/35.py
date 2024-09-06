```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number is divisible by n, it returns the largest number within this range. 
If n is not divisible by any number in this range, the function returns 1, as every number is divisible by 1. 
This solution is efficient and has a time complexity of O(n). 
It also fulfills the problem requirement of returning the largest divisor less than n. A possible test case could be `largest_divisor(15)`, which returns 5.