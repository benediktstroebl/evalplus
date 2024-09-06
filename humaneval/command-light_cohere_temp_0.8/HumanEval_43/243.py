```python
def pairs_sum_to_zero(l):
    return sum(x) < 0 for x in l
```

This function uses a list comprehension with the sum() function to generate a truthy result if there are two distinct elements in the list whose sum is less than or equal to zero, and a False otherwise.