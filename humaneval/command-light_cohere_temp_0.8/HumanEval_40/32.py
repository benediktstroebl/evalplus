```python
def triples_sum_to_zero(l):
    return sum(x for x in l if len({x, x+1, x-1}) <= 2) <= 0
```
This Python function, triples_sum_to_zero, takes a list l as input and returns a boolean indicating whether the list has three distinct elements whose sum is less than or equal to zero. The function uses a distinct elements from the list to find a sum of three numbers that add up to zero, and returns True if the sum is less than or equal to zero, and False otherwise.