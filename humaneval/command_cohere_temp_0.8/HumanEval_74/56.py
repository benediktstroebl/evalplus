```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else max(set(lst1 + lst2), key=len)
```

The code uses a simple approach to solve the problem. In essence, it checks whether the two lists have an equal number of characters, and if so, it returns the first list. If not, it takes the list with the most characters from the union of the two lists and returns it.