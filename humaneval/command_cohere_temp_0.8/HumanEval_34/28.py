```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in Python set to automatically filter out duplicate elements, and the sorted() function to sort the unique elements in ascending order. 
The script successfully passes the test cases provided in the prompt, as it produces the expected output for lists with duplicate entries, while collecting all unique elements and sorting them. 
To execute the function simply call unique() and pass the list as an argument, e.g. unique([1, 3, 3, 7, 1, 2, 11, 1, 5, 4]).