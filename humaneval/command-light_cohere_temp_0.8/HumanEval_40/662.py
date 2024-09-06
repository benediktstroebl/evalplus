```python
def triples_sum_to_zero(lst):
    if sum(set(map(sum, lst)))) == 0:
        return True
    else:
        return False
```
This function calculates the sum of distinct elements in the list and checks if it's equal to zero. If it is, the function returns True, and False otherwise.