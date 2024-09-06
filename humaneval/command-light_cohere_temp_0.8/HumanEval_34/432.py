Here's a self-contained Python function that returns unique elements in a list, passing the test:
```python
def unique(lst):
    return list(set(lst))
```
The function `unique` takes a list `lst` as input and returns a new list containing only the unique elements from the original list. 
This function uses the set() function to create a set from the input list, and then creates a new list with the unique elements from the set.