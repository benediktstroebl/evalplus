```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` takes a list as an argument and returns a list of all the positive numbers in that list. The mechanism for accomplishing this is by employing a list comprehension, which is enclosed within the function. Within the list comprehension, the elements of the list are iterated over, and those with values greater than zero are included in the new list. Everything else is excluded by the filter process. The function efficiently provides the required positive number output.