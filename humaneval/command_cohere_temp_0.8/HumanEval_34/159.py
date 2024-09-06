```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in Python set to automatically filter out duplicate elements, and then uses the sort() method to sort the values. 

Here is an example of how to use this function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [0, 2, 3, 5, 9, 123]
```
This will return the sorted list of unique elements in the input list. Adjustments might be necessary depending on the test cases required to evaluate the functionality of the function.