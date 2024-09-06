```python
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

values = ['a', 3.14, 5]
print(filter_integers(values))  # Output: [5]
``` 
This script provides a self-contained function that takes a list of values and returns a new list with only the integers from the input. The function uses the certain type testing to only return integers from the input list.