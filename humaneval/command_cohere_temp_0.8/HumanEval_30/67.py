```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` iterates over the list and filters elements that are greater than zero, returning the final list that contains only positive numbers. 

Here is an example of how to use the code:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

The output is expected to be a list that contains only the positive numbers from the provided list. 

This code uses list comprehension, which is a powerful Python feature that allows you to create a new list by applying a condition or transformation to each item in the existing list. 

List comprehension provides a concise way to handle collections of data and is commonly used in Python for filtering, mapping, and reducing sequences of data.