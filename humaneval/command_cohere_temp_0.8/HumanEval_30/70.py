```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

This Python script defines a function called `get_positive` that takes a list `l` as input. Within the function, it uses a list comprehension to iterate over each element `x` in the input list `l`. For each element `x`, it checks if `x` is greater than zero (`x > 0`). If this condition is met, the element `x` is included in the resulting list that is returned by the function. This effectively filters out all negative numbers from the input list and returns a new list containing only the positive numbers. 

This solution is concise and achieves the goal of separating positive numbers from the list, regardless of the list's content or size.