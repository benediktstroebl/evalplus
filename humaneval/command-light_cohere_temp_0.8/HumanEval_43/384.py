Here's the solution:

```python
def pairs_sum_to_zero(l):
    s, n = 0, len(l)
    for x in l:
        if s + x < 0:
            return False
        s += x
    return True
```

This function takes a list `l` of integers and iterates through the list, checking if the sum of any two adjacent elements in the list is less than zero. If a sum is always non-negative, the list passes the test. 

Note that this solution assumes the input list contains only integers.