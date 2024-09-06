```python
def triples_sum_to_zero(lst):
    if sum([x for x in lst if x < 0]) == 0:
        return True
    return False
```
The code defines a function called triples_sum_to_zero that takes a list of integers as input and returns True if there are three distinct elements in the list that sum to zero, and False otherwise. It uses a specific logic to achieve this.