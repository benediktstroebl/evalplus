```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that returns a list of positive numbers from an input list. It employs a list comprehension to iterate through each element in the input list (`l`). For each element, it checks if the element is greater than zero (`x > 0`). If the condition is satisfied, the element is included in the resulting list.

The function returns the resulting list, which contains only positive numbers. 

This approach ensures that the code remains efficient by eliminating the need for multiple passes through the input list and preserving the original list's order.