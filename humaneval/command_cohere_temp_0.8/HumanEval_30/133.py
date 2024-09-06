Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a compact way of creating a new list based on existing lists, to filter out all positive numbers from the input list `l`. It works efficiently and returns a list containing only the positive numbers present in the input list.