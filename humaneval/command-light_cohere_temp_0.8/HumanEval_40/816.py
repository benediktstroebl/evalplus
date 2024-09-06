```python
def triples_sum_to_zero(lst):
    sum_of_three = sum(x for x in lst if x != 0 and (x + x + 1) <= 3)
    return sum_of_three == 0
```
Do you have any other questions related to coding or any other topic you'd like to explore?