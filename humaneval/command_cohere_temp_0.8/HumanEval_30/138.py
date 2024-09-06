Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
The function utilizes a list comprehension to filter out elements that are not greater than zero, resulting in a new list containing only the positive numbers from the input list.