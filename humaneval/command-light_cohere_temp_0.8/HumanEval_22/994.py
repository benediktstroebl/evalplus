Here's a self-contained Python function that filters out integers from a list of any values:
```python
def filter_integers(values):
    """Filter given list of any python values only for integers
    Returns: List[int]"""
    return [x for x in values if isinstance(x, int)]
```
The function takes a list of values as input and returns a new list containing only the integers from the input list. 

It uses a list comprehension with the isinstance function to check if each element in the input list is an integer. 
This allows the function to accept any data type as input and returns a list of integers from the input list.