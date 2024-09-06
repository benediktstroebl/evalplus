```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that returns a list of positive numbers from an input list. It employs a list comprehension, iterating over each element `x` in the input list `l`. For each `x`, it checks if `x` is greater than zero (`x > 0`). If this condition is true, the respective `x` is included in the resultant list that is eventually returned. 

This solution is concise and achieves the goal of filtering only positive numbers from the input list.