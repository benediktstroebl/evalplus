```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  #STOPS WHEN j==i
            if j == i:
                return i
            if j > i:  # this condition is to make sure that i is the largest divisor
                return i
        else:
            continue
    else:
        return 1
```