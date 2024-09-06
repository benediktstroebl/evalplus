Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l: list):
    return [x for x in l if x >= 0]
```
This function uses a list comprehension, filtered for values greater than or equal to 0.