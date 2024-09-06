```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` iterates over the input list and uses a list comprehension to filter out only the positive numbers. It then returns this filtered list, ensuring that only positive numbers are retained and all other numbers are discarded. 

This approach ensures that the function is self-contained and easy to use, as it does not rely on any external variables or assumptions. 

You can easily test this function with different input lists to verify its behavior.