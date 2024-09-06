Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
The function utilizes a list comprehension, filtering out elements that are not greater than zero. This allows it to return a list containing only the positive numbers from the input list.