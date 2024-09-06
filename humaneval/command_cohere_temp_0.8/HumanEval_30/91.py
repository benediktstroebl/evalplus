```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension, iterating over each element in the input list `l`. For each element `x`, it checks if `x` is greater than zero. If the condition holds true, the element is included in the resultant list that is returned. By employing this strategy, the code efficiently isolates and retrieves only the positive numbers from the input list.