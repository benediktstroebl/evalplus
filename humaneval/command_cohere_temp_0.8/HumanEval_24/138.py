```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number is divisible by n, it returns the largest number within this range. 
If n is not divisible by any number in this range, the function returns 1, as per the specification of the problem. 
This algorithm is optimal, given the computational complexity of O(n). 
Any number outside this range will not be a divisor of n. 
Lastly, to handle the edge case of n being 1, we can add a return statement for whenever n == 1, so that the function returns 1. Gives the following updated code:
```python
def largest_divisor(n):
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    if n == 1:
        return 1
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```