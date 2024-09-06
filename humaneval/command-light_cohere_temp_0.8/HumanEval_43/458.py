```python
def pairs_sum_to_zero(l):
    return sum(x) < 0 for x in l
```
The function implements a simple algorithm to check if there exist two distinct elements in the list whose sum is less than zero, this meets the requirement to return True.

Note that the function can be easily extended to handle other data types, such as dictionaries or sets, by modifying the input parameter.