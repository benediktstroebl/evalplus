```python
def starts_one_ends(n):
    pos_num = 10**n - 10**(n - 1) + 1
    return pos_num - (pos_num - 9) / 9
```

This Python script defines a function `starts_one_ends` that calculates the number of n-digit positive integers that start or end with 1. 

The idea is to calculate the total number of `n`-digit numbers and then subtract the numbers that do not start or end with 1. 

The formula for getting the total `n`-digit numbers is `10^n - 10^{n-1} + 1`. Removing the numbers that do not start or end with 1, can be done by removing all the numbers where the first or last digit isn't 1, which is `9/9` of the total numbers. The remaining counts are the ones that have 1 as the first or last digit.